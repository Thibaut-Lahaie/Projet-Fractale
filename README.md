# SAE206
IUT INFO AIX S2 - SAE 2.06 Maths Info  
 
auteurs : Goujon William - Lahaie Thibaut - Saadi Nils - Valls Marion  
date : 05/02/2022  

*Dans le cadre d'un projet (SAE 2.06) recoupant mathématiques et informatique nous avons choisi de développer un ensemble d'activités portant sur les fractales.  
Les fractales sont des figures infiniment morcelées dont les détails se répètent en zoomant sur la figure.  
Elles ont de nombreuses propriétés liées à leur symétrie et autres caractéristiques.  
Nous avons réalisé des scripts en Python afin de construire des fractales en utilisant deux concepts mathématiques : le mot de Fibonacci et le set de Cantor.  
Afin de développer une approche plus ludique de ces notions nous avons cherché à avoir un maximum de rendus graphiques. Notre objectif est également de générer un rythme à partir du set de Cantor.*

## Composition du dossier
### Dossier Documents
Ce dossier comporte : 
- le journal de bord et l'analyse du travail réalisé (*Compte_Rendu_G1B.pdf*)
- les recherches effectuées sur le sujet traité (*Documentation_G1B.pdf*)
- le TD (*TD_G1B*) et sa correction (*TD_Correction_G1B*).  
### Dossier Codes
Ce dossier comporte :
- le code de la fractale issue du mot de Fibonacci avec Turtle (*fractale.py*)
- le code de la fractale issue du mot de Fibonacci avec PIL (*fractale_img.py*)
- le comparaison des vitesses d'exécution des algorithmes pour générer le mot de Fibonacci (*testExecutionFractale.py*)
- le code du set de Cantor avec implémentation dans un fichier (*cantorset.py*)
- le code du set de Cantor avec génération d'un son (*fractToSong.py*)

### Dossier Presentation_orale
Ce dossier comporte le diaporama pour la présentation orale de cette SAE.  

## Modules utilisés
Nous avons utilisé l'IDE Spyder où la plupart des modules en Python sont déjà installés.
Cepandant, si vous utilisez un environnement de programmation différent, voici les modules utilisés associés aux commandes pour les installer:
- PIL (génération d'images):  
```python
python3 -m pip install --upgrade pip  
python3 -m pip install --upgrade Pillow
```
- Turtle (dessin d'images progressivement):
```python
pip install turtle
```
- timeit (pour connaitre le temps d'éxéxution d'une partie de code):
```python
pip install pytest-timeit
```


