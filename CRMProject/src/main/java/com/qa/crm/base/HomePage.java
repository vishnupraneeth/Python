package com.qa.crm.base;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class HomePage extends TestBase{

 // 1) check the user name lable 
 // 2) click the contacts page link
//3) click the deals page link
//4) click the tasks link 
	
	@FindBy(xpath="//td[contains(text(),'vishnu praneeth')]")
	WebElement usrlable;
	
	@FindBy(xpath="//a[contains(text(),'Contacts')]")
	WebElement contacts;
	
	@FindBy(xpath="//a[contains(text(),'Deals')]")
	WebElement dealslink;
	
	@FindBy(xpath="//a[contains(text(),'Tasks']")
	WebElement tasklink;
	
	
	
	public HomePage() {
		
		PageFactory.initElements(driver, this);
		
	}
	
	public String usrlabldisplay() {
		String label=	usrlable.getText();
		return label;
		
	}
	
	public void contclick() {
		
		Actions action=new Actions(driver);
		action.moveToElement(contacts).build().perform();
		
		
	}
	






}
