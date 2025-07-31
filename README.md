# 🖼️ Classificateur d’Images IA (ResNet50 + Streamlit)

Cette application web permet de téléverser une image et d'obtenir une prédiction automatique de son contenu à l'aide d'un modèle d'apprentissage profond pré-entraîné (ResNet50) fourni par PyTorch.

> 🎯 Idéal pour l'apprentissage, les projets de portfolio, et la mise en pratique du transfert de connaissances (transfer learning) en vision par ordinateur.

---

## 🚀 Fonctionnalités

- 🧠 Utilise un modèle ResNet50 pré-entraîné sur ImageNet (1 000 classes)
- 📸 Accepte les images JPEG et PNG
- 📊 Affiche les 3 prédictions les plus probables avec leur score de confiance
- 🌐 Interface utilisateur simple avec Streamlit
- ✅ Fonctionne entièrement en local (aucune clé API nécessaire)

---

## 🧰 Technologies utilisées

- Python 3.x
- [PyTorch](https://pytorch.org/)
- [Torchvision](https://pytorch.org/vision/)
- [Streamlit](https://streamlit.io/)
- Pillow (PIL)
- `requests` (pour récupérer les étiquettes ImageNet)

---

## 📸 Capture d’écran (exemple)
<img width="1919" height="874" alt="Capture d'écran 2025-07-31 092913" src="https://github.com/user-attachments/assets/a7f5ce6b-01d5-452f-938e-b2b687d337c0" />

![Capture d’écran de l’application](samples/screenshot.png) <!-- tu peux ajouter une capture plus tard -->


---

## 🧠 Comment ça fonctionne ?

 -  Le modèle ResNet50 pré-entraîné est chargé depuis Torchvision

 -  L’image est redimensionnée et normalisée pour correspondre au format ImageNet

 - Le modèle effectue une prédiction


 - Les 3 classes les plus probables sont affichées avec un pourcentage de confiance


## 📈 Exemple de résultat

### Top 3 Prédictions :

 - Labrador retriever — 87,24 %

 - Golden retriever — 7,52 %

 - Cocker spaniel — 2,91 %


 ## 🛠️ Améliorations possibles

 - Téléversement de plusieurs images en une fois

 - Possibilité d’entraîner le modèle sur un dataset personnalisé

 - Affichage de l’image originale vs l’image prétraitée

 ## 👤 Auteur

 ## 📄 Licence

 MIT — libre d’utilisation, de modification et de distribution.






