# Análisis de Malware en Ingeniería Inversa
Trabajo de fin de grado de Jose Maria Gasent Zarza en Analisis de Malware e Ingenieria Inversa

## Descripción
Este repositiorio contiene los archivos del trabajo de fin de grado de José María Gasent Zarza.


## Resumen 
La ciberseguridad es un campo de la informática en constante cambio, debido a la naturaleza increíblemente reactiva del mismo. Los comúnmente conocidos como "equipo rojo" y "equipo azul", para los agentes maliciosos y los profesionales encargados de la defensa y prevención de infecciones respectivamente, se ven obligados a adaptarse a las nuevas técnicas y sistemas que cada uno usa para combatir al otro. Esto genera un entorno en constante evolución que premia no solo la capacidad, si no también la velocidad de adaptación y desarrollo de nuevas estrategias capaces de sobrepasar los estándares de seguridad usados por empresas e instituciones por parte de los atacantes, y de nuevas técnicas de detección y prevención de ataques por parte de los encargados de ciberseguridad.

Esta necesidad para superar constantemente al equipo opuesto convierte el análisis de malware en una de las capacidades más importantes para la adaptación a las nuevas técnicas usadas por grupos de actividades criminales en la red que tienen los expertos en seguridad. La posibilidad de analizar e investigar software malicioso se convierte así en una pieza clave tan esencial que gran parte del tiempo invertido en el desarrollo de malware se ve centrado en la ofuscación del código del mismo, en un intento de ralentizar, si no frenar totalmente, el análisis de este para causar así el mayor daño posible u obtener el mayor beneficio posible en el tiempo que las autoridades, infraestructuras y negocios tarden en adaptarse a cualquier nuevo cambio que se produzca en el malware.

De esta forma, en el siguiente trabajo de fin de grado se hará un estudio de algunos de las familias de malware más comunes actualmente, estudiando su comportamiento, técnicas de infección para obtener acceso a los equipos y capacidades para obtener persistencia en el equipo infectado. Muchos de estos virus ya han sido analizados extensa y exhaustivamente, y su funcionamiento interno es conocimiento publico, sin embargo, todos ellos están sujetos a la posibilidad de verse alterados para evadir nuevos métodos de detección, por lo que se hará uso de múltiples técnicas de análisis e ingeniería inversa sobre muestras recientes de virus detectados y aislados.

Se hará especial hincapié en los sistemas que usa el malware para obtener persistencia, llegando a ver el funcionamiento de los conocidos como bootkits, unos complejos tipos de rootkits que se instalan en el MBR para mantener un equipo infectado incluso después de un formateo completo del sistema operativo.

A modo de conclusión, se resumirá como evitar y detectar infecciones como las estudiadas a lo largo de este proyecto, desde un nivel de usuario hasta un nivel de administrador de equipos o redes. 

# Malware Analysis and Reverse Engineering
End of degree thesis on Malware Analysis and Reverse Engineering

## Description
This repository contains the files related to the end of degree thesis made by José María Gasent Zarza

## Abstract

Due to its incredibly reactive nature, cybersecurity is an IT field in constant change. The commonly known as "red team" and "blue team", for the malicious agents and professionals in charge of defense and prevention from attacks respectively, find themselves in a constant battle to adapt and get on top of each other's new techniques and systems. This creates an environment in constant evolution that rewards not only the capability, but also the speed to adapt and develop new strategies capable of overwhelming the security standards used by business and institutions on the side of the attackers, and new techniques to detect and prevent attacks on the side of the cybersecurity professionals.

This need to constantly surpass the opposing team makes malware analysis a capability of the utmost importance in order to adapt to the new techniques used by criminal activities groups online that security experts can posses. The ability to analyze and research  malicious software becomes such an essential key piece that a great deal of the malware's developers time and efforts are put into obfuscating the code itself, in an attempt to slow, if not completely halt, the analysis of the malware in order to be able to make the most damage or get as much of a benefit as possible in the time it takes for the authorities, infrastructure and businesses to adapt any new changes or updates on the malware.

As such, in this work we'll make a study on some of the most common malware families at the moment, studying their behaviour, the infecting methods they make use of to obtain access to machines, and their capabilities to obtain persistence in an infected system. Many of the viruses we'll see have already been exhaustively studied in length and their functionality is public knowledge, nevertheless, all of them are subject to the possibility of being altered to evade new detection methods, so we'll make use of multiple analysis and reverse engineering techniques on fresh malware samples recently discovered and isolated.

We'll take a particular interest on the methods used by malware in order to obtain persistence, going as far as to take a closer look into bootkits, a complex type of rootkit that hook themselves on the MBR nd thus obtaining persistence on an infected device even after a full wipe and reformatting of the operating system.

As a conclusion, we'll summarise how to prevent and detect infectious malware like the ones studied through this work, from an user-level viewpoint to a system or network administrator one.

