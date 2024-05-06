package co.com.project.CCSApp.task;

import co.com.project.CCSApp.userinterfaces.Home;
import co.com.project.CCSApp.utils.Constantes;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Performable;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.actions.Enter;

import static net.serenitybdd.screenplay.Tasks.instrumented;

public class PruebaRegistro implements Task {
    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(
                Click.on(Home.Registrarse),
                Enter.theValue(Constantes.nombre_user).into(Home.nombreRegistro),
                Enter.theValue(Constantes.cedula_user).into(Home.cedulaRegistro),
                Enter.theValue(Constantes.rol_user).into(Home.rolRegistro),
                Enter.theValue(Constantes.departamento_user).into(Home.departamentoRegistro),
                Enter.theValue(Constantes.correo_user).into(Home.correoRegistro),
                Enter.theValue(Constantes.telefono_user).into(Home.telefonoRegistro),
                Enter.theValue(Constantes.password_user).into(Home.passwordRegistro),
                Click.on(Home.BotonRegistro)
        );
    }

    public static PruebaRegistro pruebaRegistro(){
        return instrumented(PruebaRegistro.class);
    }
}