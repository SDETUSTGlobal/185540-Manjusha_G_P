describe('Login Page for Smartbear Software',()=> {
	it('Protractor Login', () => { 
		browser.waitForAngularEnabled(false); 
			browser.get('http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx') 
			.then(() => element(by.id('ctl00_MainContent_username')).sendKeys('Tester'))  // then keyword is used to chain
			.then(() => element(by.id('ctl00_MainContent_password')).sendKeys('test')) 
            .then(() => element(by.name('ctl00$MainContent$login_button')).click())
			browser.getCurrentUrl().then((url) => {
				expect(url).toBe('http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/default.aspx');})
		});
    it('Protractor order item', () => {
        browser.waitForAngularEnabled(false); 
        element(by.partialLinkText("Ord")).click()
        .then(() => element(by.name("ctl00$MainContent$fmwOrder$txtQuantity")).sendKeys("10"))
        .then(() => element(by.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click())
        .then(() => element(by.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Manju"))
        .then(() => element(by.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("Bgr street"))
        .then(() => element(by.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("Tvpm"))
        .then(() => element(by.name("ctl00$MainContent$fmwOrder$TextBox4")).sendKeys("Kerala"))
        .then(() => element(by.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("123"))
        .then(() => element(by.id("ctl00_MainContent_fmwOrder_cardList_0")).click())
        .then(() => element(by.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("012345"))
        element(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("12/23");
		element(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/a")).click();
		
    });
	});