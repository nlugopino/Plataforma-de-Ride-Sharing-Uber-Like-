# Plataforma de Ride-Sharing (Uber-like)

**Integrantes**
- Nelson Lugo
- Cristhian Zamora

**Grupo**
- E196

Este proyecto consiste en el diseño y desarrollo de una **plataforma de Ride-Sharing**, inspirada en servicios como **Uber**, cuyo objetivo principal es conectar pasajeros y conductores de manera eficiente, segura y dinámica.

El sistema será desarrollado utilizando **Python como lenguaje de backend**, aplicando progresivamente **patrones de software** y **buenas prácticas de arquitectura**, los cuales serán incorporados como avances durante todo el curso.

El enfoque del proyecto es principalmente **arquitectónico y académico**, permitiendo analizar cómo el uso adecuado de patrones de diseño ayuda a resolver problemas reales de escalabilidad, mantenibilidad y evolución del software.

---

## Objetivo General

Diseñar e implementar una plataforma backend modular y escalable que gestione los procesos principales de un sistema de ride-sharing, aplicando patrones de software para resolver problemas comunes del dominio.

---

## Funcionalidades Principales

### 1. Matching dinámico entre conductores y pasajeros
Asignación automática de conductores disponibles a pasajeros considerando:
- Ubicación
- Disponibilidad
- Tipo de servicio

### 2. Sistema de tráfico dinámico
Gestión de condiciones de tráfico que afectan:
- Tiempo estimado de llegada
- Rutas óptimas
- Cálculo del costo del viaje

### 3. Gestión de pagos y propinas
Procesamiento de pagos incluyendo:
- Diferentes métodos de pago
- Cálculo de tarifas
- Propinas
- Historial de transacciones

### 4. Sistema de seguridad y emergencias
Manejo de eventos críticos como:
- Alertas de emergencia
- Seguimiento del viaje
- Registro de incidentes

---

## Arquitectura General

El backend estará estructurado bajo una arquitectura modular inspirada en **Clean Architecture**, separando claramente:

- **Dominio**: reglas de negocio
- **Aplicación**: casos de uso
- **Infraestructura**: base de datos, servicios externos
- **Interfaces**: API REST

Esta separación permitirá:
- Bajo acoplamiento
- Alta cohesión
- Facilidad de mantenimito
