# 🐾 Bot Identificador de Razas de Perros y Gatos

Un bot de Discord que utiliza inteligencia artificial para identificar razas de perros y gatos a partir de una foto.

---

## 📋 Descripción

Este bot recibe una imagen enviada por el usuario en Discord, la analiza con un modelo de clasificación de imágenes entrenado en **Google Teachable Machine**, y responde indicando qué raza detectó junto con el porcentaje de confianza de la predicción.

El modelo fue entrenado con **50 imágenes por clase** y puede reconocer 4 razas: dos muy conocidas y dos poco comunes, para que sea entretenido y también educativo.

---

## 🐶🐱 Razas que identifica

| Animal | Raza | Curiosidad |
|--------|------|------------|
| Perro | Golden Retriever | Una de las razas más populares del mundo |
| Perro | Xoloitzcuintle | Raza ancestral mexicana, conocida como "el perro sin pelo" |
| Gato | Siamés | Reconocido por sus ojos azules y personalidad vocal |
| Gato | Khao Manee | Raza tailandesa, considerada símbolo de buena suerte |

---

## ⚙️ ¿Cómo funciona?

1. El usuario escribe `?check` y adjunta una foto en Discord
2. El bot descarga la imagen temporalmente
3. La redimensiona a **224x224 píxeles** (formato que espera el modelo)
4. El modelo analiza la imagen y la compara con las 4 razas aprendidas
5. Responde con la raza detectada y el porcentaje de confianza
6. Borra la imagen temporal del sistema

---

## 🤖 Comandos disponibles

| Comando | Descripción |
|---------|-------------|
| `?check` + imagen | Clasifica la raza de la foto enviada |
| `?razas` | Muestra las razas que el bot puede identificar |

---

## 📸 Ejemplo de uso

> El usuario escribe `?check` y adjunta una foto de su mascota.  
> El bot responde con un mensaje como este:

```
🔍 Resultado de Clasificación
Raza detectada: Golden Retriever
Confianza: 94.73%
Sobre esta raza: Raza muy popular, conocida por ser amigable y obediente.
```

> *(Reemplaza esta sección con una captura de pantalla real del bot en acción)*  
> `![Ejemplo del bot](enlace_a_tu_captura_aqui)`

---

## 🛠️ Tecnologías utilizadas

- **Python** — Lenguaje principal
- **discord.py** — Librería para conectar con la API de Discord
- **TensorFlow / Keras** — Para cargar y ejecutar el modelo de IA
- **Pillow** — Para procesar y redimensionar las imágenes
- **Google Teachable Machine** — Herramienta con la que se entrenó el modelo
- **python-dotenv** — Para manejar el token de forma segura

---

## 🚀 Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Crea el entorno virtual e instala las dependencias
```bash
pip install discord.py tensorflow==2.15.0 pillow numpy python-dotenv
```

### 3. Crea el archivo `.env` en la raíz del proyecto
```
DISCORD_TOKEN=tu_token_aqui
```

### 4. Asegúrate de tener estos archivos en la raíz
```
📁 tu_repositorio/
├── main.py
├── model.py
├── keras_model.h5
├── labels.txt
└── .env
```

### 5. Ejecuta el bot
```bash
python main.py
```

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.  
Puedes usar, copiar, modificar y distribuir este código libremente, siempre que se mantenga el crédito original.

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```
