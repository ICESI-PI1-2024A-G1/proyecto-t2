package co.com.project.CCSApp.task;

import co.com.project.CCSApp.userinterfaces.Home;
import co.com.project.CCSApp.userinterfaces.Login;
import co.com.project.CCSApp.utils.Constantes;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.actions.Enter;

import static net.serenitybdd.screenplay.Tasks.instrumented;

public class PruebaIngreso implements Task {

    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(
                Enter.theValue(Constantes.cedula_user).into(Login.cedulaLogin),
                Enter.theValue(Constantes.password_user).into(Login.passwordLogin),
                Click.on(Login.BotonLogin)
        );
    }

    public static PruebaIngreso pruebaIngreso(){
        return instrumented(PruebaIngreso.class);
    }
}

