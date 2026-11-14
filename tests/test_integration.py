"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D).
"""
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from api.main import app

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 : Un client ouvert par « with » exécute le lifespan."""
    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_non_charge_renvoie_503(monkeypatch):
    """D.3 : Modèle retiré de app.state -> 503."""
    with TestClient(app) as client:
        # On retire le modèle de l'état
        monkeypatch.setattr(app.state, "classifier", None)
        response = client.post("/predict", json={"text": "Un avis valide"})
        assert response.status_code == 503


def test_modele_plante_renvoie_500(monkeypatch):
    """D.4 : Simule une panne du modèle (RuntimeError) pour couvrir les lignes 77-79."""
    def predict_qui_plante(text):
        raise RuntimeError("Panne interne du modèle")
    
    with TestClient(app) as client:
        monkeypatch.setattr(app.state.classifier, "predict", predict_qui_plante)
        response = client.post("/predict", json={"text": "Un avis valide"})
        assert response.status_code == 500
        assert "Panne interne" not in response.text


def test_modele_leve_valueerror_renvoie_500(monkeypatch):
    """D.4 : Simule une ValueError pour couvrir le bloc 85-87."""
    def predict_qui_leve_valueerror(text):
        raise ValueError("bug interne")
    
    with TestClient(app) as client:
        monkeypatch.setattr(app.state.classifier, "predict", predict_qui_leve_valueerror)
        response = client.post("/predict", json={"text": "Un avis valide"})
        assert response.status_code == 500
        assert "bug interne" not in response.text