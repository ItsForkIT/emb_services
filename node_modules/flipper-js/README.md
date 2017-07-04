flipper
=======

Simple feature flipping mechanism for node and the browser


Usage:

```js
    var flipper = require('flipper');
    
    flipper.register('my-feature')
           .setCheck(function(context, done){
               //some async method to determine if it should be flipped
               done(true);
           })
           .setFlipped(function(){
               alert('flipped');
           })
           .setUnflipped(function(){
               alert('unflipped');
           });
```
