#🟡 A7 — Diseñar URLs (REST básico)

#Para un sistema de libros con autores, proponé las URLs (/algo/algo) y verbos para: listar todos los libros, ver un libro puntual, listar los libros de un autor puntual, crear un autor. Listo cuando: tus URLs usan sustantivos (recursos), no verbos (nada de /getLibros o /crearLibro), y el verbo HTTP hace el trabajo del verbo.

#Listar todos los libros: GET /libros
#Ver un libro puntual: GET /libros/42
#Listar los libros de un autor puntual: GET /autores/7/libros
#Crear un autor: POST /autores