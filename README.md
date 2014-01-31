html-deconstruct
================

HTML Deconstructor

A simple script to create a deconstructed version of some HTML to make working out the structure a little easier.

## Installation

Just need a stock python 2.x install.

## Usage

### HTML from a file:

    python htmldecon.py test.html

### HTML from stdin

    cat test.html | python htmldecon.py

Or run it without any arguments, paste in the HTML to the terminal window, and then hit ctrl-d.

### HTML from a URL

    python htmldecon.py https://github.com/tobyontour/html-deconstruct

## Cutting down HTML
###Style using only semantic HTML selectors.

So when you see:

`<div class="column-12 content">`

And the current css is:

`div.column-12 { width: 960px; }`

Re-work to:

`div.content { width: 960px; }`

### Remove non-semantic HTML
When you see:

`<div class="column-12 content">`

Change the HTML to:

`<div class="content">`

Or even:

`<article>`

### Go through each element (within reason) and strip out unused classes
Use the inspector tools in Chrome or whatever browser tools you usually use and
click on an element. If it has no rules targetting it specifically on that 
class then remove the class.

There should be a note of caution here because if there is javascript using
those classes then you will break it. If you have access (and the ability) then
you can alter the javascript to target more semantically.

If you have javascript targetting a class of 'clearfix' or 'column-12' then you
have my sympathies.

### Document autonomous chunks of HTML in a clear and semantic way
So:

    <header>
    <a id="main-content"></a>
      <h1>
        <span class="artist">{{ artwork.all_artists|capfirst }}</span>
        <span class="title-row">
          <span class="title">{{ artwork.title }}</span>
          <span class="datetext">{{ artwork.dateText }}</span>
        </span>
      </h1>
    </header>

Could become:

    header
      a#main-content
      h1
        span.artist
        span.title-row
          span.title
          span.datetext

