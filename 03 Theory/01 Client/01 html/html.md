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


##### What are the HTML media elements?

HTML media elements are used to present the audio and video.

Some of the HTML media elements are:

HTML audio element:
The HTML audio element represents a sound or audio stream. It is used to play an audio file on an HTML document.

```HTML
<audio>
  <source src="horse.ogg" type="audio/ogg" />
  <source src="horse.mp3" type="audio/mpeg" />
  Your browser does not support the audio element.
</audio>
```
The HTML source element specifies multiple alternative media resources for HTML img elements or for media elements (audio, video, etc.). 

It is commonly used to give the same media content in multiple file formats for providing compatibility across different browsers.

The HTML src attribute of the source element specifies the URL/path of the media resource.

##### HTML video element?
The HTML video element represents a video. It is used to play audio files with captions, videos or movies.

```HTML
<video>
  <source src="movie.mp4" type="video/mp4" />
</video>
```

##### How to embed an HTML document into another HTML document?
We can embed another HTML document within the current HTML document using the HTML iframe element.
```HTML 
<iframe src="https://learning.ccbp.in"></iframe>
```

The HTML src attribute specifies the URL/path of the HTML document to embed.


##### How to insert a video into the HTML document?

We can insert a video to the HTML document using:
```HTML
<video>
  <source src="movie.mp4" type="video/mp4" />
</video>
```

The HTML source element defines the media resource for the HTML video element.

The HTML src attribute specifies the URL/path of the media resource (e.g. video).
The HTML type attribute specifies the type/format of the media resource(e.g. video/mp4)


##### HTML iframe element

```Javascript
<iframe src="https://www.youtube.com/embed/y881t8ilMyc"></iframe>
```
The HTML src attribute specifies the URL/path of the video.

To have the embed link of the YouTube video, follow these simple steps:

Open the video on YouTube and click the share button.  
Open the Embed code.  
Copy the value of the src attribute and paste it into the value of the HTML src attribute of our HTML iframe element.  

##### How to set controls in HTML video element?

The HTML controls attribute is used to set controls in HTML video element. It is a boolean attribute. When this attribute is present, it specifies that video controls should be displayed.

Video controls include:

* Play
* Pause
* Seeking
* Volume
* Fullscreen toggle
* Captions/Subtitles (when available)
* Track (when available)

```Javascript
<video controls>
  <source src="movie.mp4" type="video/mp4" />
</video>
```


##### What is the use of an HTML iframe element?
Some of the uses of HTML iframe element are:

* We can embed HTML documents within the current HTML document
* We can embed videos within the current HTML document, etc.


##### What is an HTML picture element?


The HTML picture element is a container to provide multiple alternative sources for the HTML img element. It is useful in different display/device scenarios.

It can contain zero or more source elements and one HTML img element.

```HTML 
<picture>
  <source
    media="(min-width:650px)"
    srcset="
      https://d1tgh8fmlzexmh.cloudfront.net/ccbp-static-website/goldentemple1-img.png
    "
  />
  
  <source
    media="(min-width:465px)"
    srcset="
      https://d1tgh8fmlzexmh.cloudfront.net/ccbp-static-website/mysore-palace1-img.png
    "
  />
  
  <img
    src="https://d1tgh8fmlzexmh.cloudfront.net/ccbp-static-website/varanasi1-img.png"
    alt="historical places"
  />
  
</picture>
```

* The HTML srcset attribute specifies the alternative source/ path of the img element.
* The HTML media attribute specifies the media query. CSS properties will be applied based on the device type and media features like min-width, etc.

##### What are HTML Semantic Elements?

The word semantic means relating to meaning in language. 

So, the HTML semantic elements describe the meaning of content in between the start and end tags.

There are around a hundred semantic elements. Some of them are:

**Header element**  

The HTML header element defines the container of introductory information or navigation links of an HTML document.

Generally, it contains heading elements, search form, logos, etc.

```HTML
<header>
  <h1>HTML Semantic Elements</h1>
</header>
```

**Nav element**

The HTML nav element defines the section of navigation links. 

```HTML
<nav>
  <ol>
    <li><a href="#home">Home</a></li>
    <li><a href="#profile">Profile</a></li>
    <li><a href="#contacts">Contacts</a></li>
  </ol>
</nav>
```

**Main element**

The HTML main element defines the main content of an HTML document.

```HTML
<header>HTML</header>

<main>
  <p>HTML Stands for HyperText Markup Language.</p>
  <p>It describes the structure of a Web page and consists of HTML elements that tell the browser how to display the content.</p>
</main>
```

**Article element**

The HTML article element defines the complete part of an HTML document which is independent and reusable.

It can be used to represent a magazine, newspaper article, blog entry or any other independent item of content.

```HTML
<article>
  <h1>HTML</h1>
  <p>HTML Stands for HyperText Markup Language. It describes the structure of a Web page.<p>
</article>

<article>
  <h1>CSS</h1>
  <p>CSS Stands for Cascading Style Sheets. It describes the styles for the HTML documents, including design, layout, etc. </p>
</article>
```

**Section element**

The HTML section element defines the generic section of an HTML document.

It is generally used to group content that has a heading.  

The HTML section and HTML article elements are conceptually similar and interchangeable. But the HTML section element differs from article element because it isn’t necessarily self-contained (complete).

```HTML
<section>
  <h1>Uses of HTML</h1>
  <ul>
    <li>Structuring web pages</li>
    <li>Creating Hyperlinks</li>
    <li>Embedding images and videos</li>
  </ul>
</section>
```

**Aside element**

The HTML aside element defines the portion of an HTML document whose content is only indirectly related to the HTML document's main content.

It specifies the content of less importance.

It is generally used to represent sidebars or call-out boxes.

```HTML
<article>
  <h1>HTML</h1>
  <p>HTML Stands for HyperText Markup Language. It describes the structure of a Web page.<p>
</article>

<aside>
  <h1>Website</h1>
  <p>Website is a collection of webpages.</p>
</aside>
```


**Footer element**

The HTML footer element defines the footer of a page or section.

It generally contains information about the author of the section, copyright data, or links to related documents.


```HTML
<footer>
  <p>Email me at rahul@gmail.com</p>
</footer>
```

##### What are the uses of Semantic HTML?

Some of the uses of Semantic HTML are:

Accessibility: It makes web pages accessible for mobile devices and people with disabilities as well. This is because screen readers and browsers can understand the code better.

Search Engine Optimization: It improves the website Search Engine Optimization Rankings which increases the number of people that visit our webpage.

Easy to Understand: It makes our code more readable and easier to understand.

##### What are HTML non-semantic elements?

The HTML non-semantic elements don't have any meaning.

Examples: div and span.

We cannot exactly find out the type of content within the given element unlike semantic elements like h1, p, etc.


##### What are the differences between HTML semantic and non-semantic elements?


**semantic**  
semantic elements have the meaning.  
They describe the content they contain.  

**non-semantic**
non-semantic elements don't have the meaning.  
They can contain anything.  


##### What are Global attributes?
Global attributes are attributes common to all HTML elements.

They can be used on all elements, though they may not affect some elements.

Examples: class, id, title, etc.

##### What are HTML selected and multiple attributes?  
**Selected Attribute**:

It is a boolean attribute. It specifies that an option should be pre-selected when the page loads.

```HTML
<option value="Active" selected>Active</option>
```

**Multiple Attribute**:
It is a boolean attribute. It specifies whether the user is allowed to provide more than one value in an input field.

It can be used in the HTML select element.

```HTML
<label for="cars">Choose a car:</label>
<select name="cars" id="cars" multiple>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
```

##### What is an HTML required attribute

The HTML required attribute is a boolean attribute.

If present, it specifies that an input field must be filled out before submitting the form.

```HTML
<form>
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" required />
  <input type="submit" />
</form>
```

##### What is an HTML html element?
The HTML html element defines the root of an HTML document.

It is a container for all the other HTML elements.

```HTML
<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <h1>Tourism</h1>
    <p>Plan your trip wherever you want to go</p>
  </body>
</html>
```

##### What is an HTML style element?

The HTML style element contains style information for an HTML document, or part of an HTML document. It contains CSS, which is applied to the contents of the HTML document.

```HTML 
<!DOCTYPE html>
<html>
  <head>
    <style>
      h1 {
        color: red;
      }
      p {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1>Tourism</h1>
    <p>Plan your trip</p>
  </body>
</html>
```

##### What is an HTML details element?

The HTML details element defines a disclosure widget where we can see the additional information.

It has two states:

* open: We can see the additional information.
* close: We can't see the additional information. We can see only the summary.
```HTML
<details>
  <summary>Details</summary>
  Something small enough to escape casual notice.
</details>
```

The summary element defines the label or summary.

##### Why HTML 5 is best compared to old versions?

HTML 5 is the latest version of HTML.

Some of the new features added in HTML5 that make it better than HTML are:

* audio and video elements
* semantic elements like header, footer, figure, figcaption, nav, etc.
* placeholder attribute
* progress element, etc.

##### What are the different doctypes in HTML?

Some of the doctype declarations for different versions of HTML are:

**HTML5:**  
```HTML
<!DOCTYPE html>
```

**HTML4.01: (Strict doctype - Doesn't allow deprecated and presentation elements like font, etc.)**  


```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```


**HTML4.01: (Transitional doctype - Allows deprecated and presentation elements like font, etc.)**  
```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
```



</details>


---