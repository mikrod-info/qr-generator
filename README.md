# QR Generator 

![Python](https://img.shields.io/badge/Python-3.x-blue)
![qrcode](https://img.shields.io/badge/qrcode-library-green)
![Pillow](https://img.shields.io/badge/Pillow-image%20processing-orange)

## Resumen

Este script genera códigos QR en lote para vincular contenidos digitales.

Surge como complemento del proyecto [Carteles Accesibles](https://github.com/mikrod-info/carteles-accesibles), donde se requería generar múltiples QR con una estructura consistente, nombres correlativos y la posibilidad de incluir un logo institucional.

## Descripción

Este script automatiza la generación de QR a partir de URLs de carteles accesibles.

Cada QR:

- Apunta a un recurso específico 
- Puede incluir un logo centrado
- Está optimizado para su impresión
- Permite generar rangos específicos para facilitar la continuidad del proceso

## Características:

- Generación masiva por rango (`inicio` - `fin`)
- Numeración automática (`cartel-01`, `cartel-02`, etc.)
- Inserción opcional de logo centrado
- Alta tolerancia a errores (corrección de QR para mantener legibilidad)
- Exportación en formato `.png`

## Requisitos:

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)

## Uso

`python generate_qr.py <inicio> <fin>`

Ejemplo:

`python generate_qr.py 20 53`

## Estructura

```shell
qr-generator
├── assets
│   └── logo.png
├── generate_qr.py
├── output
│   ├── qr-cartel-01.png
│   ├── qr-cartel-02.png
│   ├── qr-cartel-03.png
│   ├── ...
└──── README.md
```

## Consideraciones

- El logo no debe superar más del 20-25% del tamaño del QR
- Usar alto contraste (negro sobre blanco)
- Validar el escaneo en dispositivos reales antes de imprimir
