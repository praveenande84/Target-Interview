# HTML

<details>
<summary>Introduction</summary>

### Introduction
**HTML** stands for **Hypertext Markup Language**

##### About HTML
* **HTML** stands for **Hypertext Markup Language**  
* **HTML** is used to create static web pages.
* Text Editor is the software for **HTML** coding.
* **HTML** file save with extension `.html`


##### HTML coding

**HTML** coding is a `Tag` based coding.

###### **HTML** Tags are two types  
    1. Container Tag : It has start Tag & End Tag.
    2. Empty Tag : It does not have an end tag.

`Container Tag`
   ```HTML
    <h1>Heading</h1>
    <p>Paragraph</p>
   ``` 

`Empty Tag`
 ```HTML
   <img src="image.png"/>
   <br/>
   <hr/>
   ``` 

* Attributes are used to give extra information to the html element.

* **HTML** elements tell the browser that how to display the content.

##### **HTML** document Structure  

An **HTML** document consists of three parts :
  1. DOCTYPE -> First Line containing HTML version information.
  2. Head Part -> html page configuration information. Head tag is for browser reading purpose
  3. Body part -> displaying content. Body tag is for client reading purpose

```HTML
<!DOCTYPE html>
<html>
  <head>
    Metadata elements
  </head>
  <body>
    content of webpage
  </body>
</html>
```

* **DOCKTYPE**  
  The doctype declaration tells the type/version of the HTML document to the browser.

* **Head Part**  
  The HTML head element is the container for the elements which provide extra information about the document (metadata).  
  It describes the properties of the document such as title, character set, style sheets, scripts, etc.

* **Body Part**  
  The HTML body element defines the main content of an HTML document that displays on the web page.

  It contains text content, paragraphs, headings, images, tables, links, videos, ...etc.

##### Element Syntax 
Element consist of a start tag, content, and end tag.

```HTML
<tag>Content</tag>
```

##### Attribute syntax
```HTML 
<tag attributeName="attributeValue">Content</tag>
```


##### Uses of **HTML**
* **Structuring web pages**  
   we can define the headings, paragraphs, and other contents of a web page.
* **Creating Hyperlinks**  
   we can navigate within the HTML document, to other web pages.
* **Embedding images and videos**  
   we can embed images and videos in the HTML document.

##### Advantages & Disadvantages of **HTML** 
* we can create only Static Web pages with HTML alone.
* By Combining HTML with CSS, we can create Responsive web pages.
* By Combining HTML with JavaScript, we can create dynamic web pages.


##### Difference between HTML and HTML5
HTML5 is more complete and easier than HTML4, it has lots of new tags like `<header>, <footer>, <navy>, <Audio>, <video>, <main>` ...etc.  
It also supports graphics. In the following image, we have described all the essential terms related to HTML and HTML5
</details>

<details>
<summary>Elements</summary>

### Elements

In general, HTML elements can be divide into two categories.
1. Block-Level Elements
2. Inline Elements

##### Block-Level Elements
These elements always start in a new line and take up the full width available. So, an HTML Block-Level element occupies the entire horizontal space of its parent element.
```HTML 
<h1>Heading</h1>
```

* h1
* p
* div

##### In-Line Elements
These elements do not start in a new line and only take up as much width as necessary.
```HTML
<p>I am <a href="http://www.google.com">Google</a> link</p>
```



##### Nested **HTML**
HTML elements can be nested.

It means that the HTML element can be placed inside another HTML element.

```HTML
<div>
  <h1>Heading</h1>
  <p>I am pragraph.</p>
</div>
```
</details>

</details>

---
---
---
---
---
---
---

<details>
<summary>HTML Elements</summary>

##### use of anchor element
We use the HTML anchor elements to navigate to other web resources or a specific HTML element within the HTML document. They are also called as Hyperlinks/ Links.

```HTML
<a href="URL">Content</a>
```

##### Heading & Paragraph Elements
**Heading**  
HTML defines six levels of headings.
HTML headings are defined with the h1 to h6 elements.

* The HTML h1 element defines the most important heading of an HTML document.
* The HTML h6 element defines the least important heading of an HTML document.


```HTML 
<h1>heading</h1>
<h2>heading</h2>
<h3>heading</h3>
<h4>heading</h4>
<h5>heading</h5>
<h6>heading</h6>
```

**Paragraph Element**  
The HTML p element defines the paragraph of an HTML document.
```Javascript
<p>I am Paragraph</p>
```


##### Difference between div & span Elements

**div**
The HTML div element is a block-level element

**span**
The HTML span element is an inline element

##### what is an HTML container Element
The HTML container element (div) defines a container. 

It can be used to wrap a group of elements and apply CSS styles to many elements at once.

##### What are HTML tags?
HTML Tags are like keywords that define how a web browser will format and display the content.

* With the help of tags, a web browser can distinguish between HTML elements and text.  
**Examples** : p, h1, br, hr, a, img, ul, ol, li, form, input, textarea, select, option



##### What is an HTML script element?
The HTML script element can be used to embed the JavaScript code.

It can contain scripting statements, or it points to an external script file through the src attribute.

```Javacsript
<script src="counter.js"></script>
```


##### How to add line breaks to an HTML paragraph element?
The HTML br element is used to add a line break to an HTML paragraph element. It breaks the text and continue it in the next line.

It is useful in writing poems, addresses, etc.
The HTML br element is a void element.
```Javascript
<h1 class="heading">
  Twinkle Twinkle Little Star
</h1>
<p>
  Twinkle, twinkle, little star, <br />
  How I wonder what you are! <br />
  Up above the world so high, <br />
  Like a diamond in the sky.
</p>
```

##### How to display images on the web page?
We can display images on the web page using the HTML img element.

Generally, the HTML img element requires two main HTML attributes.

src specifies the path to the image.

alt specifies an alternate text for the image.
```Javascript 
<img src="IMAGE_URL" alt="image" />
```

##### What are the attributes we can give to an HTML image element?
The attributes we can give to an HTML image element:  
src
alt
height
width
class, etc.

##### What is an HTML image element?
The HTML img element defines an Image.
```Javascript 
<img src="IMAGE_URL" alt="image" />
```

##### Does a hyperlink only apply to text?
We can use hyperlinks to text as well as images, buttons, etc.

```Javascript
<a href="link"> Link Text </a>
<a href="link"> <button>Click Here</button> </a>
<a href="link"> <img src="image.png" /> </a>
```

##### How to create a link in HTML and what is the HTML target attribute?

The HTML anchor element can be used to create the links on a web page.

It requires the HTML href attribute to specify the URL/ path of the page where the link goes to.
HTML target attribute:

The HTML target Attribute specifies where to open the linked web resource.

It can have the following values:

**_self** :	(Default value) It opens the document in the same window or tab as it was clicked.  
**_blank** :	It opens the document in a new window or tab.  
**_parent** :	It opens the document in a parent frame.  
**_top** :	It opens the document in a full-body window.


##### What is the difference between HTML anchor element and HTML link element?

* **HTML anchor element**  
  We use the HTML anchor element to navigate to other web resources or a specific element within the HTML document.

* **HTML link element**  
  We use the HTML link element to link the HTML and CSS files.

##### What is the difference between HTML script element and HTML link element?

* **HTML script element**
  We use the HTML script element to embed the JavaScript code to HTML file.
* **HTML link element** 
 We use the HTML link element to link the HTML and CSS files. 

##### What are the differences between the HTML ordered List and the HTML unordered List?

* **HTML ordered list**  
  It is created using the ol element.  
  It is a collection of related items that follow some order or have a sequence

* **HTML unordered list**
  It is created using the ul element.  
  It is a collection of related items that have no special order or sequence.

##### Explain types of lists in HTML?
There are three types of lists in HTML:

* Unordered list: It is used to group a set of related items in no particular order.

* Ordered list: It is used to group a set of related items in a specific order.

* Description list: It is used to display name/value pairs such as terms and definitions.


##### Explain the HTML hr (horizontal line) element?

The HTML hr element inserts a horizontal line and helps to separate the content.


##### Explain about the HTML block-level elements and inline elements?

**Block-level Elements**:

The HTML Block-level elements always start in a new line and take up the full width available. 

So, an HTML Block-level element occupies the entire horizontal space of its parent element.

Examples: HTML h1 element, HTML p element, HTML div element, etc.

**Inline Elements**:

The HTML Inline elements do not start in a new line and take up the content width.

Examples: HTML button element, HTML img element, HTML a element, etc.

##### Why Meta elements are used in HTML?

* Meta elements can contain information about character encoding, description, title of the document etc.  
* Meta elements are used to tell the browser about the page description, author of the template, character set, keywords, etc.  
* Meta elements are used for search engine optimization to tell the search engine about the page contents.


</details>

---

<details>
<summary>HTML Attributes & General</summary>

### HTML Attributes & General

##### href attribute

The HTML href attribute is the most important attribute of the HTML anchor element.

It specifies the URL/path of the page the link goes to.  
The value of the HTML href attribute is URL/path of the page where the link goes to.

##### class attribute

The HTML class attribute is used to specify a class name for an HTML element.

##### id attribute
The HTML id attribute specifies a unique id for an HTML element. The value of the id attribute must be unique within the HTML document.

* It can be used for styling an HTML element using CSS.  
* It is also used by JavaScript to access and manipulate the HTML elements with the specific id.

##### Name some of the attributes used in HTML?

class, 
id, 
href, 
src, 
for, 
width, 
height, 
name, 
alt, 
style, 
checked, 
type etc,...

##### What are the HTML attributes?

The HTML attributes provide additional information about HTML elements. 

They are always specified in the start tag.  
They usually come in name/value pairs like: name="value"  
Examples: src, style, alt, etc.



##### Difference between id & class

###### id 
The HTML id attribute specifies a unique id for an HTML element.  
It is used to apply styles to a single element.  
The id must be unique within the HTML document. There shouldn't be more than one element with the same id.  

###### class
The HTML class attribute specifies a class name for an HTML element.  
It is used to apply styles to multiple elements with the class name.  
One or more HTML elements can have the same class name.  

##### Can multiple HTML elements have the same id?
No. There shouldn't be more than one HTML element with the same id.

The id must be unique within the HTML document.

##### Can we use the HTML p element inside an HTML span element?  
The HTML span element is an inline element, which should contain only other inline elements.

So as span is an inline element and p is a block-level element, we can't use the p element inside a span element.

Note
Not all the HTML inline elements should contain only other inline elements. There are few exceptions for it. Example: HTML anchor element, etc.  

##### What is the difference between HTML and JavaScript?
JavaScript is a programming language that makes web pages more interactive and dynamic.  
HTML is a markup language that is used to describe the structure and layout of web pages.  

##### What is a viewport?
**Viewport**: The browser's viewport is the area of the window in which web content can be seen.

##### differences between HTML and Python?
**Python**  
Python is an interpreted, object-oriented, high-level programming language.  
It is generally used to instruct a computer to perform certain actions on an input and return an output.  

**HTML**  

HTML is a markup language that is used to describe the structure and layout of web pages.  
It is generally used to format the output (How to appear on a website).  	

</details>

---

<details>
<summary>HTML Forms & Tables</summary>

#### HTML Forms & Tables

##### Explain HTML form element?

The HTML form element can be used to create HTML forms. It is a container that can contain different types of elements like,

* input
* label
* select
* textarea
* button
* fieldset
* legend
* data list
* output
* option
* optgroup, etc.

##### What are forms and how to create forms in HTML?
The form is used to collect the user inputs. HTML provides a form element to create forms.  

```Javascrip 
<form action="/submit_data.php">
  <label>Enter your name: </label>
  <input type="text" name="name" />
  <label>Enter Mobile number </label>
  <input type="number" name="mobile_no" />
  <input type="submit" value="Submit" />
</form>
```

##### What is checkbox and how to use checkbox?
To define a Checkbox, We need to specify the HTML type attribute with the value checkbox for an HTML input element.

```Javascript 
<input type="checkbox" id="vehicle1" name="vehicle1" value="Bike1" />
<input type="checkbox" id="vehicle2" name="vehicle2" value="Bike2" />
```

##### What are the differences between the HTML checkbox and radio input elements?

##### HTML radio input element:

* It is used when only one option to be selected out of several available options.  
* It is created by using an HTML input element with the type attribute value is set to radio.

##### HTML checkbox input element:

* It is used when more than one option to be selected out of several available options.  
* It is also created by using the HTML input element with the type attribute value is set to checkbox.  


##### What is an HTML checked attribute?

The HTML checked attribute specifies that an input element should be pre-selected (checked) when the page loads.  

```HTML
<input type="radio" id="genderMale" value="Male" name="gender" checked />
```

##### How to create a combobox in HTML?
The HTML select element is used to create a combobox or drop-down list of options. 

The HTML option element should be inside the HTML select element for defining options in the drop-down list.

```HTML
<select>
  <option>option1</option>
  <option>option2</option>
</select>
```
</details>

---

<details>
<summary>More Interview Questions</summary>

</details>


---