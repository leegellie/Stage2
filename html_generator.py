section_titles = [['Section 1','''Lee's Notes So Far (Stage 2 - Work Session 1)'''],
                  ['Section 2','''Stage 2 &mdash; Intro to "Serious" Programming'''],
                  ['Section 3','''Stage 2 &mdash; Variables &amp; Strings'''],
                  ['Section 4','''Stage 2 &mdash; Input&rarr;Function&rarr;Output'''],
                  ['Section 5','''Stage 2 &mdash; IF &amp; WHILE'''],
                  ['Section 6','''Stage 2 &mdash; Structured Data''']]
sections_list = [['Section 1','World Wide Web','''The World Wide Web is a collection of computers that can communicate with each other to share html and source files for other computers on the WWW to view.'''],
                 ['Section 1','Major Pieces of the Web','''                <ul>
					<li><span class="content">You</span></li>
                    <li><span class="content">Your Computer &#43; Browser</span></li>
                    <li><span class="content">The Internet</span></li>
                    <li><span class="content">Servers</span></li>
				</ul>'''],
                 ['Section 1','HTML is','''				<ul>
				  	<li><span class="content">Text content &mdash; What you see</span></li>
			        <li><span class="content">Markup &mdash; Code to display</span></li>
			        <li><span class="content">References to other documents &mdash; e.g. images &amp; videos</span></li>
					<li><span class="content">Links to other pages</span></li>
				</ul>'''],
                 ['Section 1','Parts of HTML','''				<ul>
				  <li><span class="content"><b><em>Tags</em></b> - Opened and closed with &lt; &amp; &gt; respectively.</span></li>
                    <li><span class="content"><b><em>Elements</em></b> - Everything from an opening tag to it's closing tag, with everything in between. </span></li>
				</ul>'''],
                 ['Section 1','Inline &amp; Block Elements','''Some elements can be &quot;inline&quot; which meants they would go along in a sentance as if it was a word. Others can be &quot;block&quot; which means that the computer sees it as having its own space and breaks out of the line to put a box around it.'''],
                 ['Section 1','HTML Code Structure','''HTML code must be structured for ease of use and accuracy in editing. Without your code structured it is very hard to make your web page look like anything but a basic word document. With structure from the apropriate elements such as DIV tags and such you can then manipulate these with CSS to look and act like anything you want.'''],
                 ['Section 1','Avoid Repetition','''Repeating styling codes not just wastes space and creates bigger, bulkier files but it also makes it harder to change document-wide styles and structure. Starting at top level selectors like classes and pseudo tags can make it easy to quickly change the whole appearance of a web page. For more precise and individual formatting selectors such as IDs and attributes can be used which, as the are more specific selectors, will only edit the styles for the specific tags even if a higher selector is modifying them.'''],
                 ['Section 1','Summary for Lessons 1 &amp; 2','''        	<span class="summary">All HTML is broken down into elements that are made up of tags, attributes and content.</span></p>
            <p><span class="summary">Formatting the elements in your code to display the HTML and CSS will let you make just about anything visible to the viewer of your web page.</span>'''],
                 ['Section 1','Summary for Lesson 3 (Big Ideas)','''<span class="summary">Using CSS you can get all the boxes and inline text to act as you want. You do this by using selectors. Selectors can be tags, classes, ids, attributes, seudo tags and pseudo elements. You then assign properties (style) to those selectors and anything that has the selector will be styalized as defined.</span></p>
            <p><span class="summary">To get the desired result of a web page that looks like a design you go through a cycle of </span><span class="quote">CODE &rarr; TEST &rarr; REFINE</span><span class="summary"> until you get the document laid out the way you want. You start this by;</span></p>
<ol>
              <li><span class="summary">Looking for the natural boxes of the design</span>.</li>
              <li>Look for repeat styles and syntax elements so that these can be given grouped classes or other selectors.</li>
              <li>(CODE) Write the HTML. </li>
              <li>(CODE) Write the styles in CSS starting from the more broad aspects and then going down to the smaller details. </li>
              <li>(TEST) Test and (REFINE) fix the things that are not correct by repeating steps 3 &amp; 4.</li>
            </ol>'''],
                 ['Section 2','Computer Programming vs. Computer Science','''Computer Science is the more abstract study of what a computer is capable of computing and to a degree most CS classes and individuals have some programming experience and/or instruction so as to test those capabilities.</p>
                <p>Computer Programming is the action of writing code to make the computer do what you need it to, or want it to.'''],
                 ['Section 2','Programming','''Programming is basically the language written to make the computer do what you want.  If there was no program, a computer would be a useless pile of metal and plastic. Just like telling someone to go to the fridge and get a drink, a computer comands in the same way.'''],
                 ['Section 2','Programming Languages','''There are many, many programming languages and there are interpreter programs that will take your commands and relay them to the computer.  Unlike spoken languages which can be ambiguous, programing languages are usually very strict. One mistake in pages of code can cause the whole thing to fail or give a wrong result.'''],
                 ['Section 2','Programming Grammar','''Programs, like spoken languages, have a set of gramatical rules. However, as mentioned above, they are very strict. Where in a sentance you may have <span class="quote">subject &rarr; verb &rarr; noun</span> you have <span class="quote">non-terminal &rarr; replacement &rarr; terminal</span> in a language such as Python.</p><p>From what I can see so far the program gives a<span class="highlight"> command </span>such as print (to display on screen) then has an<span class="highlight"> expression </span>(which can be a number or even a result of another fuction), and then an<span class="highlight"> operator </span>(the thing that will calculate, modify or in some other way compute) and then a final<span class="highlight"> expression.</span> I am sure there are other ways we will learn to code but that does the simple arithmatic.</p>'''],
                 ['Section 2','Summary for Stage 2 Intro to "Serious" Programming','''<span class="summary">Programming is a precise series of commands and values that will result in the computer giving back or displaying certain result or following certain commands.</span></p>
            <p><span class="summary">For the code written in an interpreter program we can get all the acceptable expressions and "grammar" to write code that can be executed by that interpreter.  If you do not follow this grammar you will get a failed result. For example, if you wanted to display the number of kids in the school and you only had the number in each class, you could put <span class="quote">print 23 + 12 + 20</span> and get the result. If you did not enter it grammatically corect and did <span class="quote">print 23 &#43; 12 &#43; 20 &#43;</span> or <span class="quote">print 23 &#43; 12 &#43; 20 &#43;</span> or <span class="quote">print 23 12 20</span> or any other number of incorect possibilities you would not get a valid result.'''],
                 ['Section 3','Variables','''Variables are used in most programming. The are something that is defined for the current program.  This action is called "assigning a variable".  It usually consists of a name and then an exuals sign, and then the value, text or other variable, or combination thereof, being assigned that name. i.e. <span class="quote">name = 'Lee Gellie'</span> or <span class="quote">sum = 4 + 2 </span></p>
            <p>In the Python program, and most programming, <span class="quote">the = in a variable is not just 'equals', it means 'assignment'.</span><span class="quote_red"> It does not mean summation!</span>'''],
                 ['Section 3','Comments','''Comments can be defined in Python code using a <span class="quote">#</span>. When doing this, everything behind the # will be commented and not read in executing the code. In python each line is a command so this does not need to be closed, it ends when the line ends.  It is very useful in making notes so you, or others, can recognize what the code is doing or why you went about it a certain way. </p>
			<p>For example; </p>
			<p><span class="quote">var = 38 * 365.25</span><span class="quote_red"> #I wanted to calculate how many days I have been alive, I am 38</span>'''],
                 ['Section 3','Linear Code','''In Python code the commands are linear. If you assign a variable you can then just call the variable again and again as needed. However, you can, later in the code, change that variable and all future references will use that new variable. Any code before the new assignment of the variable will use the original variable value.</p>
            <p>In this way you can have something like this;</p>
        <p class="quote">count = 1<br>
          print count
            <br>
          count = count + 1
          <br>
          print count
          <br>
          count = count + 1
          <br>
          print count
          <br>
          count = count + 1
          <br>
          print count<br>
          count = count + 1
          <br>
          print count
          <br>
          count = count + 1
          <br>
          print count
          <br>
          count = count + 1
          <br>
        print count          
        <p><span class="content">Which would return;</span></p>        
        <p><span class="quote">1<br>
        2<br>
        3<br>
        4<br>
        5<br>
        6<br>
      7</span>'''],
                 ['Section 3','Strings','''Strings are generally text values. The will be defined with a start and an end quote. Such as <span class="quote">'Lee'</span> or </span><span class="quote">"Lee"</span>.  The quotations that you start and end with must be the same. You can not start with a single and end with a double. If you do not end a quote it will be an error.</p>
			<p>This makes it very handy for using the other kind in the text as EVERYTHING will be concidered text until you have closed the quotation. So you can write <span class="quote">print &quot;Lee's mum is going to the 'new' house today!&quot;</span>. This would return a value of <span class="quote">Lee's mum is going to the 'new' house today!</span>'''],
                 ['Section 3','Strings &amp; Numbers','''Python can not add strings and numbers. <span class="quote_red">print "Joe" + 39</span> would be an error. If you wanted to add text and a number you could do this by assigning a variable such as;</p>
		<p><span class="quote">age = 38<br>
		  text = 'Joe is '<br>
		end = '.'</span></p>
		<p><span class="quote">print text + age + end</span></p>
		<p>The result would be;</p>
		<p><span class="quote">Joe is 38.</span>'''],
                 ['Section 3','Selecting Sub&ndash;Sequences','''If you add opening and closing square brackets after a variable calling a string you can use this to numerically select parts of that string.</p>
            <p>All string selecting starts with '<span class="quote">0</span>' and goes up numerically to however long the string is. You can select by numbering from the back of the line starting at -1 and work your way toward the beginning. So to select the second character of the variable <span class="quote">string = plop</span> you would need to type <span class="quote">string[1]</span> and the result would be '<span class="quote">l</span>'.</p>
            <p>You can also select multiple characters from the string by using 3 spaces in the square bracket represented as Number&ndash;Colon&ndash;Number, or Start&ndash;Colon&ndash;Stop. You do not, in fact, have to have a number before or after the colon but this is the easiest way to think of it.  If you have nothing before the colon it will start from the beginning of the string. If you put a numerical value it will start from that column of the string.  The colon means 'go up to'. And then you have the final number space, which will take everything from the beginning or the defined start and go up to <span class="quote_red">JUST BEFORE</span> the final number. So if the last character was 23 and you typed <span class="quote">string[1:4]</span>, you would get from the 2nd, remember  it starts on 0, to the second last charcter. So, in the above example you would get returned <span class="quote">lo</span>.  Again, if you leave the end number blank it will go to the end. If you typed <span class="quote">string[1:]</span> you would get returned <span class="quote">lop</span>.  So if you left both numbers blank <span class="quote">string[:]</span> you would get from the beginning to the end, so <span class="quote">plop</span>.'''],
                 ['Section 3','Using the Find Operation','''The find command can be used in the following format <span class="quote">string_var.find(string)</span></p>
            <p>It will search from the beginning of the string until it finds the first instance of the search parameter.  It will then return the numerical column that the first part of the parameter was found. If it does not find it at all it will return <span class="quote_red">-1</span>.</p>
            <p>You can define where the search starts by typing <span class="quote">string_var.find(string, 14)</span> which will have the search start on the 15th character in the string.'''],
                 ['Section 3','Summary for Stage 2 &ndash; Variables &amp; Strings','''<span class="summary">Programming is a precise series of commands and values that will result in the computer giving back or displaying certain result or following certain commands.</span></p>
            <p><span class="summary">For the code written in an interpreter program we can get all the acceptable expressions and "grammar" to write code that can be executed by that interpreter.  If you do not follow this grammar you will get a failed result. For example, if you wanted to display the number of kids in the school and you only had the number in each class, you could put <span class="quote">print 23 + 12 + 20</span> and get the result. If you did not enter it grammatically corect and did <span class="quote">print 23 &#43; 12 &#43; 20 &#43;</span> or <span class="quote">print 23 &#43; 12 &#43; 20 &#43;</span> or <span class="quote">print 23 12 20</span> or any other number of incorect possibilities you would not get a valid result.</span>'''],
                 ['Section 4','Concepts of Input&rarr;Functions&rarr;Output','''In the most simplistic terms you enter something into a computer, calculator, toaster or whatever and it does something in some way to give an output. In Python you define things and give it data, which can be strings or numbers, and have the program in some way use the code to produce something which will then be returned or given back as a result. Every line after the defining of the function name must be indented. </p>
            <p>For example if I wrote;</p>
            <p><span class="quote">def say_hello(name):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;greeting = "Hello " + name + "!"<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return greeting</span></p>
            <p>I would get the result;</p>
            <p><span class="quote">print say_hello("Miriam")<br>
            print say_hello("Andy")</span></p>
            <p>The "Mirriam" & "Andy" would be input. The code to create the statement would be the function and the result and what were displayed would be the output.'''],
                 ['Section 4','Using a Procedure (Function)','''You can set (make) procedures by using a def command at the beginning and it won't use it unless called upon later in the code. It will be there and be dormant until you set a command to run that procedure and then return it's value.</p>
            <p>To set a procedure the basic code is to give it a name, for example <span class="quote">jojo</span>, then you have opening and closing parentheses with any input value you want to pull in them separated by commas. So something like <span class="quote">jojo(a,b)</span></p>
            <p>There can be as many inputs as you want as long as you separate them with commas and give that many inputs.</p>
            <p>If you are defining a procedure you put def before it and a colon after and then on the next line you put the function(s) you would like run.</p>
            <p>You end up with something like this;</p>            
            <p><span class="quote">def add_two_numbers(number_1, number_2):<br>
    		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return number_1 + number_2</span></p>
			<p>You could then give the command along with the input;</p>
			<p><span class="quote">print add_two_numbers(4, 3)</span></p>
			<p>And you would get the result <span class="quote">7</span>.</p>
			<p>An important thing to remember is that you must have an output for your function. You can do all the clever stuff you want but without a return your print statement will still be blank.'''],
                 ['Section 4','Example of Creating HTML in Python','''In this example I want to create a div block that has in it an h1 tag with a title that is variable and a content that is variable. </p>
			<p>
			<span class="quote">def create_html(title,content):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;html_element_1 = """<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;div class='box_container'&gt;<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;div class='box_title'&gt;<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1 class='title'&gt;""" + title + &quot;&lt;/h1&gt;&quot;<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;html_element_2 = """<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;article class='box_content'&gt;<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;p class='content'&gt;""" + content + &quot;&lt;/p&gt;&quot;<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;html_element_3 = """<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/article&gt;<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;&quot;&quot;&quot;<br>
            <br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;html_total = html_element_1 + html_element_2 + html_element_3<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return html_total<br>
            <br>
            div_title = 'This is The Title'<br>
            div_content = 'This is the content to my article.'<br>
            <br>
            print create_html(div_title, div_content)<br></span>
			<p>This would then output;</p>
			<pre class="quote_red" data-ng-show="stdout">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;div class='box_container'&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;div class='box_title'&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1 class='title'&gt;This is The Title&lt;/h1&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;div class='box_content'&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;p class='content'&gt;This is the content to my article.&lt;/p&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;</pre>'''],
                 ['Section 4','Summary for Stage 2 &ndash; Input&rarr;Function&rarr;Output','''<span class="summary">As long as you remember to close and check all formatting the general rules are pretty easy. If you are running into trouble in your coding you can alway put print commands to help show you where it is going wrong.</span></p>
            		<p><span class="summary">Using code like this can help programmers avoid having to repeat things over and over as they can code to pull, for example, all the first names for a mailing list, have it put their name after "Dear " and add a "," after wich they can have a whole letter and print that letter. Thus with very little code you could send out a whole mailing that is individually addressed. </span>'''],
                 ['Section 5','Making Decisions with Code','''The operators for making decisions in Python give a boolean (true or false) result. Some of the things we looked at are <span class="quote">greater than</span> (<span class="quote">&gt;</span>), <span class="quote">less than</span> (<span class="quote">&lt;</span>), <span class="quote">equal to</span> (<span class="quote">==</span>) and <span class="quote">not equal to</span> (<span class="quote">!=</span>). The double equals symbol is used as the single equal symbol is already used to assign variables.'''],
                 ['Section 5','Using the IF Function','''To use the if function type if &lt;expression&gt;: then below and indented you have the &lt;block&gt; which will define what code is run if the expressions is TRUE. If the expression is false it will skip this code. </p>
            <p>With the IF function you can also define an ELSE statement.  This means that if your IF runs a false result it will then go to the else statement and run what is there. The ELSE must be on the same indentation as the IF, as in the example below;</p>
            <p><span class="quote">def bigger(num_1,num_2):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;if num_1 &gt; num_2:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return num_1<br>
			&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if num_1 &lt; num_2:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return num_2<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:      <br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if num_1 == num_2:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return num_1<br></span></p>

            <p>This code will always return the greater of two numbers input. </p>
            <p>If you are telling the code to return True or False you must capitalize as below;</p>
            <p><span class="quote">def is_friend(name):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;if name[0] == 'D':<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True<br>
            &nbsp;&nbsp;&nbsp;&nbsp;else:<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return False</span></p>
            <p>In the above example you can simplify it by just asking for the value as the double equals sign is already testing true or false. You could then have something like this to get the same result;</p>
            <p><span class="quote">def is_friend(name):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;return name[0] == 'D'</span></p>
            <p>Some people like to have all the statements but it is not necessary.</p>            
			<p>You could also give an or statement if you want to check against several values being True;</p>
            <p><span class="quote">def is_friend(name):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;return name[0] == 'D' or name[0] == 'N'</span>'''],
                 ['Section 5','Evaluating IF and OR','''When a function, such as <span class="quote">IF</span> or <span class="quote">OR</span> is called to evaluate two or more expressions it will stop at the first <span class="quote">TRUE</span> expression. So if you said <span class="quote">Am I 8 or 9?</span> and you were 8, it would return <span class="quote">True</span>.  It would never actually evaluate whether you were 9 or not as it knows at least one of the statements is true already. If you were 9 and asked the same question it would evaluate the 8 as <span class="quote_red">FALSE</span> but then go onto the 9 and return <span class="quote">TRUE</span>.</p>
			<p>So if you needed to test both expressions you may need to just put <span class="quote_red">False</span> in the first to ensure that there is no error in the second, as it will not pass the first expression if it returns a <span class="quote">TRUE</span> value. It would then have to evaluate that second expression and tell you if there was an error in it.'''],
                 ['Section 5','The MAX command','''Working out how to get the biggest number from 3 different numbers can easily be done with the MAX command which will automatically give you the largest of any amount of inputs. You would write it;</p>
            <p><span class="quote">max(a,b,c,etc...)</span>'''],
                 ['Section 5','This IS Basic Programming','''With just the data learned so far all computing can be done!  What this means in essence is that all computing breaks down to arithmetic and evaluating and using these basic principles one could, theoretically, recreate or write any computer code.</p>
            <p>However, almost all computer programming is done on a base that has many other preset procedures, or functions, that will make it much easier than writing out huge long codes.'''],
                 ['Section 5','Loops','''A loop is basically a way of repeating a certain action. We are starting with the <span class="quote">WHILE</span> loop.</p>
			<p>The <span class="quote">WHILE</span> loop starts with an expression that will validate the running of the loop followed by a colon. This is called a test expression. Inside of that we have the block that will run as long as the test expression is <span class="quote">TRUE</span>.  The difference between this and the <span class="quote">IF</span> command is that once it runs the command it will go back to check if the test expression is still <span class="quote">TRUE</span>.  If it is, it will run the block of code again, and it will keep doing that until the test expression shows a <span class="quote_red">FALSE</span> value.</p>
			<p><span class="quote">i = 0<br>
            while i &lt; 10:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;print i<br>
			&nbsp;&nbsp;&nbsp;&nbsp;i = i + 1</span></p>
			<p>This will result in the code printing from 0 to 9. Once it gets to 10 it is no longer less than 10 so the code will not work. </p>
			<p>An Infinit Loop is one that never finds a false value so will keeo running indefinitely.'''],
                 ['Section 5','Break Statement','''A break gives you a way to stop the loop even if the condition is still <span class="quote">TRUE</span>.</p>
			<p>You could stick this in an <span class="quote">IF</span> command in the <span class="quote">WHILE</span> loop which will check to see if there is a reason to break the process or let it continue. If this IF statement is <span class="quote">TRUE</span> and you break out of the loop you will then continue the code after the while loop. If it the IF statement is <span class="quote_red">FALSE</span> it will continue to run the code and the loop and will check the <span class="quote">IF</span> statement again next time around.'''],
                 ['Section 5','Summary for Stage 2 &ndash; If &amp; While Functions','''<span class="summary">The </span><span class="quote">IF</span><span class="summary"> and </span><span class="quote">WHILE</span><span class="summary"> functions can be extremely useful and make life a lot easier for a programmer as you can automate when and for how long (or how many times) code steps get carried out.  Without them you would have to write code for every possible occurrence and it could be very lengthly and extensive to code.</span></p>
           		  <p><span class="summary">From counting to greeting according to time of day, these functions can make it very simple to code aspects that would otherwise take a lot of consideration and figuring.</span>'''],
                 ['Section 6','List Function','''It is similar to a string, in that it is a type of structured data.  But a string is limited as it is strictly text data. </p>
                <p>In a list you can have any kind of data.  In a string instead of using quotation marks you use square brackets and you divide the data with comments, like so; <span class="quote">[a,b,'yoy','flop',4]</span>.</p>
                <p>If you had the string;</p>
                <p><span class="quote">s = [a,b,'yoy','flop',4]</span></p>
                <p>You can still use the square brackets to call data from it like;</p>
                <p><span class="quote">s[3]</span></p>
                <p>Return would be 'flop'.</p>
                <p>If you selected multiple values, as;</p>
                <p><span class="quote">s[3:4]</span></p>
                <p>You would get returned a list and the return would be;</p>
                <p><span class="quote">['flop',4]</span></p>
                <p>You can make a list with no elements<span class="quote"> []</span>, known as an 'empty list' or any number from one element upwards. Like in strings, the first element is referred to as <span class="quote_red">0</span>.</p>
                <p>You can also have a list inside of a list, in which case you just add a set of square brackets in between the commas of you original list and populate it as you would a normal list.</p>
                <p>If you have to divide a list onto more than one like you should try and do it after a comma in the list.</p>
                <p>If you need to get an element out of a list inside a list you would just ad a second square bracket after the first.</p>
                <p><span class="quote">a[2][3]</span></p>
                <p>This would give you the 4th nested list item in the 3rd list item of the main list.'''],
                 ['Section 6','Mutation','''Mutation means we can change the value of a list after it has been created. 
So if you had a list <span class="quote">p = ['H','e','l','l','o']</span>.</p>
		<p>You could replace the <span class="quote_red">'H'</span> to <span class="quote_red">'Y'</span> by redefining the first element of the list like this: <span class="quote">p[0] = 'Y'</span></p>
            <p>Strings are not able to be changed. Lists have a big advantage there.'''],
                 ['Section 6','Aliasing','''Is when you have 2 different names for the same object.  If you change one then the other will also change.'''],
                 ['Section 6','Append Function','''Like find you have &lt;list&gt; <span class="quote">.append(&lt;element&gt;)</span> This will affix an element to the end of a list. It will not make the list different. This will add whatever is in the append into it's own list item. if you wanted to add several items into the list you would have to use the PLUS function as the append would make a new list inside of the original list as one item on the end. Basically it means add one list item containing...'''],
                 ['Section 6','Plus Function','''You can add a <span class="quote">plus sign</span> between two or more lists and it will give you an output of a list combined of all the items in each list added together.'''],
                 ['Section 6','Len Function','''<span class="quote">len(&lt;list&gt;)</span> The LEN operator is short for Length.  It also works for strings. If you put a list inside the length operator it will return the number of base list items in the list. If you have a list inside the list it will still only count it as one item.</p>
		<p>If you use the length operator on a string it will count the number of characters in the string.'''],
                 ['Section 6','Append, Plus and Len','''If you had </p>
            <p><span class="quote">p = [1,2]</span></p>
        <p><span class="quote">q = [3,4]</span></p>
            <p>And appended them: p.append(q)</p>
            <p>You would get <span class="quote">len(p) = 3</span> as the list would have appended q as one list item. So p would now refer to: <span class="quote">[1,2,[3,4]]</span> Which is three base list items.</p>
        <p>If you wanted to add them you would use the plus, like so;</p>
            <p><span class="quote">p = [1,2]</span></p>
            <p><span class="quote">q = [3,4]</span></p>
        <p><span class="quote">p = p + q</span></p>
            <p><span class="quote">len(p)</span> now = 4, <span class="quote">[1,2,3,4]</span>'''],
                 ['Section 6','For Loops','''A for is used as follows;</p>
            <p><span class="quote">for &lt;name&gt; in &lt;list&gt;:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&lt;block&gt;</span></p>
            <p>What it means is that for each element in the list, we are going to assign that element a name and evaluate the block. And it will do that in order until it has done all elements in the list.'''],
                 ['Section 6','Index Function','''The index element is used similar to the find element. </p>
		<p>The format is <span class="quote">&lt;list&gt;.index(&lt;value&gt;)</span> If the value entered is in the list then it will return the first occurrence of that value in the lest.  If it not in the list it will return the error <span class="quote_red">"&lt;value&gt; is not in the list."</span>'''],
                 ['Section 6','In Function','''Syntax is <span class="quote">&lt;value&gt; in &lt;list&gt;</span>.&nbsp; It is Boolean. You can use <span class="quote">NOT IN</span> which would of course reverse the <span class="quote">True</span> or <span class="quote_red">False</span>.'''],
                 ['Section 6','Summary for Stage 2 &ndash; Structured Data','''<span class="summary">The </span><span class="quote">IF</span><span class="summary"> and </span><span class="quote">WHILE</span><span class="summary"> functions can be extremely useful and make life a lot easier for a programmer as you can automate when and for how long (or how many times) code steps get carried out.  Without them you would have to write code for every possible occurrence and it could be very lengthly and extensive to code.</span></p>
           		  <p><span class="summary">From counting to greeting according to time of day, these functions can make it very simple to code aspects that would otherwise take a lot of consideration and figuring.</span>''']]
				  
def compile_HTML():   
    print '''<html>
    <head>
        <title>This is my HTML Page Created in Python</title>
        <link href="styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div id='container'>
            <h1>Lee's Class Notes<br>
            Nanadegree - Introduction to Programming</h1>'''
    print '            <h2>Sections Index</h2>'
    for header in section_titles:
        html_index_sect_num = header[0]
        html_index_sect_title = header[1]
        html_index = html_index_sect_num + ': ' + html_index_sect_title
        print '''            <h3>''',html_index,'''</h3>'''
    for section in section_titles:
        section_num = section[0]
        section_desc = section[1]
        print '''            <div class='section_content'>
                <div class='section_head'>
                    <h1>''' + section_num + ': ' + section_desc + '''</h1>
                <div>'''
        for para in sections_list:
            para_sect = para[0]
            para_head = para[1]
            para_note = para[2]
            if para_sect == section_num:
                print '''                <article class='note'>
                    <h2>''' + para_head + '''</h2>
                    <p>''' + para_note + '''</p>
                </article>'''
        print '''            </div> <!-- Close Section Div -->'''
    print '''        </div> <!-- Close Container Div -->
    </body>'''
   
compile_HTML()