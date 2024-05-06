# Created by Isabella at 4/05/2024
Feature: Test para el registro de un usuario a la aplicacion

  Scenario:
    Given Soy un usuario sin credenciales registradas
    When ingreso los datos para crear mi usuario
    And le doy al boton registrar
    Then quedo registrado exitosamente en el sistema