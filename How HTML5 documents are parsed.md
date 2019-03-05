
## **Overview**

Parsing is an essential process for browser's rendering engine which basically translates the HTML document to a structure which a the browser's code can use.
The process is based on a syntax rules which the HTML document obeys which is specified by W3 org.
The result of parsing is usually a tree of nodes i.e the structure of the document.  

1. The input to the HTML parsing consists a stream of unicode characters, which is passed through tokenization stage followed by a tree construction stage
The output is document object.
  * For HTML it is the DOM Tree
  * For CSS it is the CSSOM Tree.

**The whole process can be summarised as:**

                         "Bytes ==> Characters ==> Tokens ==> Nodes ==> DOM"

![Browser Processing  ](https://kbassets.sgp1.digitaloceanspaces.com/1551774311886-full-process.png)

2. The input stream referred above is actually a sequence of bytes which is coming either over a network or your local file system.
3. The bytes encode characters in a particular encoding which the browser uses to decode the bytes into characters.

As mentioned above, HTML parsing contains two processes tokenization and tree construction.

#### **Tokenization:**
  It is the process of breaking down a sequence of character into `HTML tokens` like `start tags, end tags, attribute names, attribute values`.
The tokenizer recognizes the token, gives it to the tree constructor, and consumes the next character for recognizing the next token, and so on until the end of the input.
> Without the tokenization process, the browser would just render characters in the input stream as text displaying the html file as it is without rendering it into a webpage.

The EOF file is indicated by document.close() or if there is a lack of any further characters in the input stream
