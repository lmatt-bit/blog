Title: An example of extension method & generic method in c#
Date: 2014-08-14 06:43
Author: lmatt wang
Slug: An-example-of-extension-method-generic-method-in-csharp

Extension methods are defined as static methods but are called by using
instance method syntax. Their first parameter specifies which type the
method operates on, and the parameter is preceded by the
**[this](http://msdn.microsoft.com/en-us/library/dk1507sz.aspx)**
modifier. Extension methods are only in scope when you explicitly import
the namespace into your source code with a <span
class="input">using</span> directive.

A generic method is a method that is declared with type parameters

<p>
This example include Extension method & generic method:

<script src="https://gist.github.com/lmatt-bit/2ce8e1419ebcbd5d6ab9.js"></script>
</p>

