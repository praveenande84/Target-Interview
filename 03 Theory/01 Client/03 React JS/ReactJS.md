# React JS

##

<details>
<summary>Index</summary>

### Index
   - Introduction
   - React Hooks
   - Redux
</details>

##

<details>
<summary>Introduction</summary>

### Introduction

##### React JS
ReactJS is an open-source JavaScript library. It was developed by Facebook.  
* ReactJS is used for building user interfaces.  
we can create **Single Page Applications (SPA)** by using ReactJS 
* React allows us to create reusable components.  
 
 ##### Advantages of ReactJS
 * Easy to Learn
 * Large Community
 * Open Source
 * Reusability of components
 * Virtual DOM

##### ReactDOM
ReactDOM is the JavaScript library that allows React to interact with the DOM.

##### React JSX
React JS introduced a new HTML like syntax named JSX to create elements.

```javascript
const element = <h1 className="greeting">Hello World!</h1>;


```

Web browsers are capable to read the regular JS objects but not the JSX. Web browsers cannot read JSX directly.
JSX needs to be converted to the regular JS object by using Babel.

##### React Fragment
The Fragment is an alternate way to return a single JSX element. It groups a list of children without adding extra nodes to the DOM.

```javascript
const Welcome = () => (
  <>
    <h1>Hello, User</h1>
    <p>You are learning React</p>
  </>
);

export default Welcome;
```

</details>

##

<details>
<summary>React Hooks</summary>

### React Hooks

   - useState
   - useEffect
   - useContext
   - useMemo
   - useReducer
   - useReference
   - useCallback
   - useCustomHook

</details>

## 

<details>
<summary>Redux</summary>

### Redux
</details>

##

<details>
<summary>Tricky Questions</summary>

### Tricky Questions

##### Why react is faster than JS?
React is a JavaScript library, thus React is not faster than JavaScript.

</details>

##