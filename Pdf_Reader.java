package com.selenium;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.net.MalformedURLException;
import.java.net.URL;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class Pdf_Reader {
WebDriver driver;

	@BeforeClass
	public void setUp() {
		System.setProperty("webdriver.chrome.driver", "C:\\Selenium Libraries\chromedriver_win32\chromedriver.exe"");
		driver=new ChromeDriver();
	}
	
	@Test
	public void PrintPDFText() throws MalformedURLException, IOException, InterruptedException {
	
		driver.get("http://localhost:1180/SAMPLE-PDF-FILE.pdf");
		String output=null;
		URL urlOfPdf = new URL(driver.getCurrentUrl());
		BufferedInputStream fileToParse = new BufferedInputStream(urlOfPdf.openStream());
		PDDocument document = PDDocument.Load(fileToParse);
		output = new PDFTextStripper().getText(document);
	}
}
