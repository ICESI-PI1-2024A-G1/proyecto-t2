package co.com.project.CCSApp.userinterfaces;

import net.serenitybdd.screenplay.targets.Target;

public class Home {
    public static Target Registrarse = Target.the("Registrarse - Inicio de Registro").
            locatedBy("#boton_registrar");

    public static Target nombreRegistro = Target.the("Nombre del user de Registro").
            locatedBy("#id_nombre");

    public static Target cedulaRegistro = Target.the("Cedula del Registro").
            locatedBy("#id_cedula");

    public static Target rolRegistro = Target.the("Rol del usuario").
            locatedBy("#id_rol");

    public static Target departamentoRegistro = Target.the("Departamento del usuario").
            locatedBy("#id_departamento");

    public static Target correoRegistro = Target.the("Correo del usuario").
            locatedBy("#id_correo_electronico");

    public static Target telefonoRegistro = Target.the("Telefono del usuario").
            locatedBy("#id_telefono");

    public static Target passwordRegistro = Target.the("Contraseña del usuario").
            locatedBy("#id_password");
    public static Target BotonRegistro= Target.the("Buton").
            locatedBy("#RegistrarUboton");


}
