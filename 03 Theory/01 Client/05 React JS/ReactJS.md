# React JS

<details>
<summary>Index</summary>

### Index

* Introduction
* Component Life Cycle
* DOM
* Class Component
* Functional Component
* state
* props
* React Hooks
* Redux
</details>

---

<details>
<summary>Introduction</summary>

### Introduction

##### React JS
__React JS__ is an open-source JavaScript library. It was developed by Facebook.  
   * ReactJS is used for building user interfaces.  
   * we can create __Single Page Applications (SPA)__ by using ReactJS .
   * React allows us to create __reusable components__. 

 ##### Advantages of ReactJS
 * Open Source
 * Easy to Learn
 * Large Community
 * Reusability of components
 * Virtual DOM


  ##### React Version
  react@17.0.0

  ##### React Components
  In __React JS__, there are 2 components
  * Class Component
  * Functional Component
</details> 

---

<details>
<summary>Component Life Cycle</summary>

### Component Life Cycle
It is a different stages of the Component during its existence.
* Mounting
* Updating
* Unmounting

##### Mounting
In the Mounting phase, the instance of a component is created and inserted into the DOM.

##### Updating
In Updating phase, the component is updated whenever there is a change in the component's state. 

##### Unmounting
In Unmounting phase, the component instance is removed from the DOM. 

</details>

---

<details>
<summary>DOM</summary>

### DOM
__DOM__ stands for __Document Object Model__ .  
* The DOM is __UI__ of your application.
* It is the structured representation of the HTML document created by the browser. 
* It allows JavaScript to manipulate, structure, and style your website.


##### Types Of DOMs
  * Real DOM
  * Virtual DOM

##### ReactDOM
__ReactDOM__ is the JavaScript library that allows React to interact with the Real DOM.

```Javascript 
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root'),
)
```


##### Real DOM
__HTML DOM__ is called __Real DOM__.

##### Virtual DOM
* DOM is created by React JS is called Virtual DOM.
* The virtual DOM is only a virtual representation of the DOM.
* when any changes are made on __UI__ then new Virtual DOM is created.
* React compares new virtual DOM with current virtual DOM, and the difference will be updated to the Real DOM.

</details>

---

<details>
<summary>Unidirectional</summary>

### Unidirectional
* The data flow of React is a Unidirectional data flow.

* Unidirectional data flow means a one-way data flow where the data has only one way to be passed to all the child components.

It means only one component can maintain and update the state. The state is passed to the child components through props.

When we want to update the state by the event triggered in the child component, we can't directly change the props in child components as props are read-only.

Thus, the state only gets updated in the parent component as props are read-only. The state is passed to all the child components through the props.

Some of the advantages of Unidirectional data flow are:

* we have more control over the data
* Easier to debug as we know what data is coming from where

![Unidirectional Data Flow](./assets/dataflow.jpg)

</details>

<details>
<summary>Component</summary>

### Component
A Component is a JS function that returns a JSX element.

```Javascript 
const Welcome = () => <h1 className="message">Hello, User</h1>;
```

* If function name starts with Capital letter then only react treats as Component otherwise react treats as HTML Element.
* We can call the function with self-closing tags `<Welcome />`.

##### Types of Components in __React JS__

1. Class Component
2. Functional Component


</details>

---
<details>
<summary>Class Component</summary>

### Class Component
* If function name starts with Capital letter then only react treats as Component otherwise react treats as HTML Element.
* The component name should always be in the pascal case.
* Class Component we can call as stateful Component.
 * A class component requires you to extend from React Component and create a render method that returns a JSX element.
```Javascript
import { Component } from "react";

class App extends Component {

  // Updating
  render() {

    // Return JSX
    return <div>App Component</div>;
  }
}
```

##### __extends__ keyword
The `extends` keyword is used to inherit methods and properties from the `React.Component`.

##### class Component Life Cycle Methods
* Mounting
  - constructor
  - render
* Updating
  - render
    - componentDidMount 
* Unmounting
  - componentWillUnmount


##### render
 - `render()` method is used to return the JSX that is displayed in the UI.
 - `render()` is called whenever the props are updated and state is updated using setState method.
 - If more than one HTML element is to be rendered, then they must be grouped using a container element or react fragment.
 - 
##### componentDidMount
The componentDidMount method is used to do operations on the components after the initial render.  
In General we make API Calls inside componentDidMount() so that it doesn't block render().
__Example__: Setting timers, initiating API calls, ...etc. 

##### shouldComponentUpdate
It is invoked before rendering when new props or state are being received. It returns true by default. If it returns false, the render method will not be called.

##### componentDidUpdate
It is invoked immediately after updating occurs. This method is not called for the initial render.

##### componentWillUnmount 
It is invoked immediately before a component is unmounted and destroyed. All the cleanup activity is performed in this method. Examples: Canceling network requests, cleaning up any subscriptions, etc.

</details>

---

<details>
<summary>Functional Component</summary>

### Functional Component
  * A functional component is just a JavaScript function that accepts props as an argument and returns a React element.
  * There is no render method used in functional components.
  * If component have don't have any state, then It is called Stateless component.
  * React lifecycle methods `(constructor, componentDidMount, componentWillUnmount, render ...etc.)` cannot be used in functional component.

```Javascript 
const App = () => {
  return (
    <div>App Component</div>
  )
}
```
</details>

---

<details>
<summary>state</summary>

### state
* State is created and managed within the component, similar to a variable declared within the function.
* State is used to store the component's data that changes over time.
* We can update state
  - `setState` method
  - `useState` hook
* when the state changes, automatically the component re-renders.
* If we try to update the state directly then it won't re-render the component.
  
</details>

---

<details>
<summary>props</summary>

### props
* Props stands for Properties.
* We can pass information from __Parent Component__ to __Children Component__ by using props.
* we can pass information throung attributes.
* The children component accept props as parameters and can be accessed directly.
*  Child Component can't change the props.


##### Parent Component
```Javascript 

```

##### Child Component
```Javascript 

```

##### key prop in list items
Keys help React identify which items have changed, are added or are removed. Keys should be given to the elements inside the array to give the elements a stable identity.

##### children prop
Children is a prop  that allow you to pass components as data to other components. Component tree put between component's opening and closing tag will be passed to that component as children prop.

```Javascript 
const Message = (props) => {
const first = props.children[0]
const last = props.children[1]
return (
   <div>
      {first}
      {last}
  </div>
);

}

export default Message
```

```Javascript 
import Message from './components/Message';

const App = () => (
  <Message>
    <span>Hello</span>
    <span>World</span>
</Message>
)

export default Message
```


##### Prop Drilling
Prop Drilling is a process in which Props are passed from one Component to another Component that does not need the data but only helps in passing it through the tree.



##### Default Props
When a component is rendered through the __route__, some of the additional props are passed.

They are:

* __match__: The match object contains the information about the path from which the component is rendered.
* __history__: The history object has some methods to control the navigation in the browser. It also maintains the history of the routes we navigated. Some of the methods to control the navigation are history.push, history.replace, etc.
* __location__: The location object contains the information about the current URL.

</details>

---

<details>
<summary>Routing</summary>

### Routing
* Routing in __React JS__ is a mechanism that allows you to navigate and display different views or components in a single-page web application.

* 
It enables users to move between different parts of the application without the need for a full page reload. `react-router-dom` is a popular library used for implementing routing in React applications.

```Javascript 
// ----->> src/components/Header/index.js <<-----
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/greeting">Greeting</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Header;
```

```Javascript 
// ---------------------------->> src/App.js <<-----------------------------------
import { BrowserRouter, Route, Switch } from "react-router-dom";

import { Home } from "./components/Home";
import Header from "./components/Header";

const Greeting = () => <h1>Welcome to React Routing</h1>;

const NotFound = () => <h1>Not Found</h1>;

const Home = () => <h1>Home Route</h1>;

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/greeting" component={Greeting} />
        <Route component={NotFound} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
```

</details>

---

<details>
<summary>React Context</summary>

### React Context
React Context is a mechanism to avoid prop drilling.

Prop Drilling means passing data from one Component to another Component that does not need the data but only helps in passing it through the tree.

</details>

---

<details>
<summary>React Hooks</summary>

  * useState
  * useEffect
  * useContext
  * useMemo
  * useReducer
  * useReference
  * useCallback
  * useCustomHook
  
### React Hooks
</details>

---

<details>
<summary>Redux</summary>

### Redux
</details>

---

<details>
<summary>Component Styles</summary>

### Component Styles
we can style the React Component by using:
* Inline Styles
* CSS Stylesheet
* Bootstrap
* Styled Components (Third Party Packages)


##### Styled Components
Styled Components are one of the new ways to use CSS in modern JavaScript. These are used to reuse styles.

We can use the third-party package `styled-components` to write Styled Components in the React Application.

```Javascript 
import styled from "styled-components";

export const Heading = styled.h1`
  color: #0070c1;
  font-family: "Roboto";
`;
```

```Javascript 
import "./App.css";
import { Heading } from "./styledComponents";

const App = () => <Heading>Hello World</Heading>;

export default App;
```
</details>

---
<details>
<summary>General</summary>

### General

##### React JSX
* React JS introduced a new HTML like syntax named JSX to create elements.
* Web browsers can only read regular JS.
* Web browsers cannot read JSX directly.
* JSX needs to be converted to the regular JS by using Babel.

##### JSX syntax
```javascript
const element = <h1 className="greeting">Hello World!</h1>;
```

##### Babel converted JSX to Regular JS
```Javascript 
const elementProps = { className: "greeting", children: "Hello World!" };
const element = React.createElement("h1", elementProps);
```

We can write a React component without using JSX.
anything you can do with JSX can also be done with just JavaScript.


##### Babel
* Babel Javascript code compiler.
* Babel converts JSX into regular JavaScript.

##### React Fragment
The __Fragment__ is an alternate way to return a single JSX element. It groups a list of children without adding extra nodes to the DOM.

```javascript
const Welcome = () => (
  <>
    <h1>Hello, User</h1>
    <p>You are learning React</p>
  </>
);

export default Welcome;
```

##### __controlled__ and __uncontrolled__
* Controlled Component :  
  In a Controlled Component, form data is handled by a React Component. 

* Uncontrolled Component :  
  In an Uncontrolled Components, form data is not handled by a React Component. It is handled by the real DOM itself.


##### SPA
__SPA__ stands for __single page application__
* In a single page application, all URLs are associated with a single HTML page.
* React is mainly used to build single-page applications.
* Single Page Application helps in faster page loading since they load only necessary Component (HTML, CSS, JS) resources on subsequent requests.

##### MPA 
__MPA__ stands for __Multi-page application__
* In a Multi-page application,
Every URL is associated with corresponding resources (HTML, CSS, JS).


##### npm 
__npm__ stands for __node package manager__

##### package.json
All npm packages contain a file, usually in the project root, called package.json

This file holds various metadata relevant to the project.
This file is used to give information to npm that allows it to identify the project as well as handle the project's dependencies.
It can also contain other metadata such as a project description, the version of the project in a particular distribution, license information, even configuration data.

```JSON 
{
  "name": "myapp",
  "version": "0.0.0"
}
```
</details>

---

<details>
<summary>API</summary>

### API
__API__ stands for __Application Programming Interface__


##### API integration
The API integration can be defined as the process of   creating a means for two or more APIs to share data and communicate with each other without human interruption.


##### axios
Axios is a third-party package for making HTTP requests.

It is similar to the fetch method.

* Installation Command
  `npm install axios`

* Uses
  - `axios.get(URL, CONFIG)`
  - `axios.post(URL, CONFIG)`
  - `axios.put(URL, DATA, CONFIG)`
  - `axios.delete(URL, CONFIG)`
</details>

---

<details>
<summary>Authentication</summary>

### Authentication
Authentication is the process of verifying a user's identity.
![Authentication and Authorization](./assets/authentication.png)
</details>

---

<details>
<summary>Tricky Questions</summary>

### Tricky Questions

##### Why react is faster than JS?
Actually __react__ is a JavaScript library, SO React is as fast as javascript.

</details>

---

