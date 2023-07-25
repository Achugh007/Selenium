package com.selenium;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.NoAlertPresentException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeDriverService;

public class Prompt {

    public static void main(String[] args) throws NoAlertPresentException, InterruptedException {
        System.setProperty(ChromeDriverService.CHROME_DRIVER_SILENT_OUTPUT_PROPERTY, "true");
        System.setProperty("webdriver.chrome.driver", "C:\\Selenium Libraries\\chromedriver_win32\\chromedriver.exe");

        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        driver.get("http:/localhost:1180/prompt.html");

        driver.findElement(By.id("submit")).click();

        Alert alert = driver.switchTo().alert();

        alert.sendKeys("Alex");
        Thread.sleep(1000);

        String alertMessage = alert.getText();

        System.out.println(alertMessage);
        Thread.sleep(5000);

        alert.accept();

        driver.quit();
    }
}
