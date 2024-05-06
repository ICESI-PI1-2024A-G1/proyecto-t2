# Created by Isabella at 5/05/2024
Feature: Test para la creacion de programas academicos en la plataforma

  Scenario:
    Given Soy un usuario con credenciales registradas
    When entro a la aplicacion del CCSA
    And entro a la seccion de gestion de la informacion
    And entro a crear nuevo programa
    And ingreso los datos para el programa
    Then el programa creada regristrado