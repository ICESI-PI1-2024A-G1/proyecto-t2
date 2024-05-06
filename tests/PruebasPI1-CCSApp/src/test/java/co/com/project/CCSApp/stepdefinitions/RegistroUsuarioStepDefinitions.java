package co.com.project.CCSApp.stepdefinitions;


import co.com.project.CCSApp.runners.RegistroUsuario;
import co.com.project.CCSApp.task.*;
import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.github.bonigarcia.wdm.WebDriverManager;
import net.serenitybdd.screenplay.actions.Open;
import net.serenitybdd.screenplay.actors.OnStage;
import net.serenitybdd.screenplay.actors.OnlineCast;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static net.serenitybdd.screenplay.actors.OnStage.theActorCalled;
import static net.serenitybdd.screenplay.actors.OnStage.theActorInTheSpotlight;
import static org.junit.Assert.assertEquals;

public class RegistroUsuarioStepDefinitions {

    WebDriver driver;

    @Before
    public void setTheStage(){
        WebDriverManager.chromedriver().clearDriverCache().setup();
        OnStage.setTheStage(new OnlineCast());
        theActorCalled("Isabella");
        driver = new ChromeDriver();
    }

    @Given("Soy un usuario sin credenciales registradas")
    public void soy_un_usuario_sin_credenciales_registradas() {
        theActorInTheSpotlight().wasAbleTo(Open.url("http://127.0.0.1:8000/"));
    }
    @When("ingreso los datos para crear mi usuario")
    public void ingreso_los_datos_para_crear_mi_usuario() {
        theActorInTheSpotlight().attemptsTo(PruebaRegistro.pruebaRegistro());
    }
    @When("le doy al boton registrar")
    public void le_doy_al_boton_registrar() {

    }
    @Then("quedo registrado exitosamente en el sistema")
    public void quedo_registrado_exitosamente_en_el_sistema(){
    }
}
