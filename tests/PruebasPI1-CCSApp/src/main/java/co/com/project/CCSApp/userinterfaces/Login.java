package co.com.project.CCSApp.userinterfaces;

import net.serenitybdd.screenplay.targets.Target;

public class Login {

    public static Target cedulaLogin = Target.the("Cedula del usuario").
            locatedBy("#id_cedula");

    public static Target passwordLogin = Target.the("Password del usuario").
            locatedBy("#id_password");
    public static Target BotonLogin = Target.the("Iniciar sesion").
            locatedBy("#boton_iniciar");

}
