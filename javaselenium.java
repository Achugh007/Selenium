import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestPromptPopUp {

    @Test
    public void testPromptPopUp() {
        WebDriver driver = new ChromeDriver();
        driver.get("prompt.html");

        // Click on the "Enter Your Name" button.
        driver.findElement(By.id("enterName")).click();

        // Enter your name in the prompt pop-up.
        String name = "Bard";
        driver.executeScript("prompt('Please enter your full name:', '" + name + "')");

        // Check if the greeting message is displayed correctly.
        WebElement greetingTextDiv = driver.findElement(By.id("greetingText"));
        String expectedGreeting = "Hello " + name + ", Enjoy browsing through this web application!";
        String actualGreeting = greetingTextDiv.getText();
        assertEquals(expectedGreeting, actualGreeting);

        driver.quit();
    }

    private void assertEquals(String expectedGreeting, String actualGreeting) {
        if (expectedGreeting.equals(actualGreeting)) {
            System.out.println("The greeting message is displayed correctly.");
        } else {
            throw new AssertionError("The greeting message is not displayed correctly.");
        }
    }
}
