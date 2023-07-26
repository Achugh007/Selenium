//package com.selenium;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.net.URL;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

public class PDFTextExtractor {

    public static void main(String[] args) throws IOException {
        // URL of the PDF file to extract text from
        String pdfUrl = "http://localhost:1180/Lorem.pdf";

        // Fetch text from the PDF file
        String extractedText = extractTextFromPDF(pdfUrl);
        System.out.println(extractedText);
    }

    public static String extractTextFromPDF(String pdfUrl) throws IOException {
        URL urlOfPdf = new URL(pdfUrl);
        BufferedInputStream fileToParse = new BufferedInputStream(urlOfPdf.openStream());
        PDDocument document = PDDocument.load(fileToParse);

        // Extract text from the PDF
        String text = new PDFTextStripper().getText(document);

        document.close();
        return text;
    }
}
