package co.com.project.CCSApp.stepdefinitions;


import co.com.project.CCSApp.task.*;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.github.bonigarcia.wdm.WebDriverManager;
import net.serenitybdd.screenplay.actions.Open;
import net.serenitybdd.screenplay.actors.OnStage;
import net.serenitybdd.screenplay.actors.OnlineCast;
import org.openqa.selenium.WebDriver;

import static net.serenitybdd.screenplay.actors.OnStage.theActorCalled;
import static net.serenitybdd.screenplay.actors.OnStage.theActorInTheSpotlight;
import static org.junit.Assert.assertEquals;

public class IngresoUsuarioStepDefinitions {

    WebDriver driver;

    @Before
    public void setTheStage(){
        WebDriverManager.chromedriver().clearDriverCache().setup();
        OnStage.setTheStage(new OnlineCast());
        theActorCalled("Isabella");
        //driver = new ChromeDriver();
    }

    @Given("Soy un usuario con credenciales registradas")
    public void soyUnUsuarioConCredencialesRegistradas() {
        theActorInTheSpotlight().wasAbleTo(Open.url("http://127.0.0.1:8000/"));
    }
    @When("ingreso los datos para iniciar en mi usuario")
    public void ingresoLosDatosParaIniciarEnMiUsuario() {
        theActorInTheSpotlight().attemptsTo(PruebaIngreso.pruebaIngreso());
    }
    @When("le doy al boton iniciar sesion")
    public void leDoyAlBotonIniciarSesion() {
    }

    @Then("entro a la aplicacion del CCSA")
    public void entroALaAplicacionDelCCSA() {
    }
}
