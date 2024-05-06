package co.com.project.CCSApp.runners;

import io.cucumber.junit.CucumberOptions;
import net.serenitybdd.cucumber.CucumberWithSerenity;
import org.junit.runner.RunWith;

@RunWith(CucumberWithSerenity.class)
@CucumberOptions(features = "src/test/resources/features/ingresoUsuario.feature",
        glue = "co.com.project.CCSApp.stepdefinitions",
        snippets = CucumberOptions.SnippetType.CAMELCASE)
public class IngresoUsuario {

}