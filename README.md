![alt text](https://yt3.ggpht.com/a-/AAuE7mAQox-RNLVUSg2hWFhsB5E8oWOtHprcJI08zA=s288-mo-c-c0xffffffff-rj-k-no)
# Mozilla Developer Network Tutorial
## Learning Web Development

### Sections Completed:
- [x] Django web framework (Python) overview
- [x] Introduction
- [x] Setting up a development environment
- [x] Django Tutorial: The Local Library Website
- [x] Django Tutorial Part 2: Creating the skeleton website
- [x] Django Tutoiral Part 3: Using Models
- [X] Django Tutorial Part 4: Django admin site
- [X] Django Tutorial Part 5: Creating our home page
- [ ] Django Tutorial Part 6: Generic list and detail views
- [ ] Django Tutorial Part 7: Sessions framework
- [ ] Django Tutorial Part 8: User authentication and permissions
- [ ] Django Tutorial Part 9: Working with forms
- [ ] Django Tutorial Part 10: Testing a Django web application
- [ ] Django Tutorial Part 11: Deploying Django to production
- [ ] Django web application security
- [ ] DIY Django mini blog



---
> _**Working Point**_:

> ## Advanced configuration


- Django does a pretty good job of creating a basic admin site using the information from the registered models:
> - [CURRENT SECTION: Book detail page - URL mapping](class BookDetailView(generic.DetailView):
    model = Book)
---
> Project Location on Github [Link](https://github.com/mdn/django-locallibrary-tutorial)
---
> ### [Django Documentation](https://docs.djangoproject.com/en/2.1/)
> #### [Django Admin Site Doc](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/)
---
> [ :ocean: ](http://localhost:8000/admin/)
---
> [Markdown List](https://guides.github.com/features/mastering-markdown/)
---
>[github emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)
---
>[Bacon Ipsum](https://baconipsum.com/?paras=5&type=all-meat&start-with-lorem=1)

---
Symbol | Meaning

------- | ----------
^ 	| Match the beginning of the text
$ 	| 	Match the end of the text
\d 	| 	Match a digit (0, 1, 2, ... 9)
\w 	| 	Match a word character, e.g. any upper- or lower-case character in the alphabet, digit or the underscore character (_)
+ 	| 	Match one or more of the preceding character. For example, to match one or more digits you would use \d+. To match one or more "a" characters, you could use a+
* 	| 	Match zero or more of the preceding character. For example, to match nothing or a word you could use \w*
( ) 	| 	Capture the part of the pattern inside the brackets. Any captured values will be passed to the view as unnamed parameters (if multiple patterns are captured, the associated parameters will be supplied in the order that the captures were declared).
(?P<name>...) 	| 	Capture the pattern (indicated by ...) as a named variable (in this case "name"). The captured values are passed to the view with the name specified. Your view must therefore declare an argument with the same name!
[  ] 	| 	Match against one character in the set. For example, [abc] will match on 'a' or 'b' or 'c'. [-\w] will match on the '-' character or any word character.