<div class="problem-statement">
   <div class="header">
      <h1 class="title">I. Расписание</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Как же Илье надоело учиться! Сначала школа, потом университет... Вот, наконец, наступил тот долгожданный день, когда Илье
            утром не надо ехать на учебу. Но, к несчастью для Ильи, оказалось, что после окончания университета начинается самое трудное&nbsp;&mdash; надо устраиваться на работу. 
         </p></span><p>Во всемирно известной фирме &laquo;Goondex&raquo;, в которую устроился Илья, принято очень много работать, в частности, для сотрудников установлена шестидневная рабочая неделя.
         Но, в качестве бонуса, &laquo;Goondex&raquo; каждый год предлагает своим сотрудникам выбрать любой день недели в качестве выходного. В свою очередь, оставшиеся шесть
         дней недели будут рабочими. 
      </p>
      <p>Илья сообразил, что с учётом государственных праздников (которые всегда являются выходными) с помощью правильного выбора выходного
         дня недели можно варьировать количество рабочих дней в году. Теперь он хочет знать, какой день недели ему следует выбрать
         в качестве выходного, чтобы отдыхать как можно больше дней в году, или, наоборот, демонстрировать чудеса трудолюбия, работая
         по максимуму. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входных данных находится одно целое число <span class="tex-math-text">N</span> (<span class="tex-math-text">0 &le; N &le; 366</span>)&nbsp;&mdash; количество государственных праздников. 
         </p></span><p>Во второй строке содержится одно целое число <span class="tex-math-text">year</span> (<span class="tex-math-text">1800 &le; year &le; 2100</span>)&nbsp;&mdash; год, в который необходимо помочь Илье. 
      </p>
      <p>В каждой из последующих <span class="tex-math-text">N</span> строк расположено по паре чисел <span class="tex-math-text">day</span> <span class="tex-math-text">month</span> (<span class="tex-math-text">day</span>&nbsp;&mdash; целое число, <span class="tex-math-text">month</span>&nbsp;&mdash; слово, между <span class="tex-math-text">day</span> и <span class="tex-math-text">month</span> ровно один пробел), обозначающих, что день <span class="tex-math-text">day</span> месяца <span class="tex-math-text">month</span> является государственным праздником. 
      </p>
      <p>В последней строке расположено слово <span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/ZGF5XF9vZlxfd2Vlaw==.png"></span>&nbsp;&mdash; день недели первого января в год <span class="tex-math-text">year</span>.
      </p>
      <p>Гарантируется, что все даты указаны корректно (в том числе указанный день недели первого января действительно является днём
         недели первого января соответствующего года <span class="tex-math-text">year</span>) и все дни государственных праздников различны. 
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите через пробел два дня недели&nbsp;&mdash; лучший и худший варианты дней недели для выходного (то есть дни недели, для которых достигается соответственно максимальное
            и минимальное количество выходных дней в году). Если возможных вариантов ответа несколько, выведите любой из них. 
         </p></span></div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>2
2015
1 January
8 January
Thursday
</pre></td>
            <td><pre>Monday Thursday
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>3
2013
1 January
8 January
15 January
Tuesday
</pre></td>
            <td><pre>Monday Tuesday
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>3
2013
6 February
13 February
20 February
Tuesday
</pre></td>
            <td><pre>Tuesday Wednesday
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Рассмотрим подробно <span style="font-weight:bold;">третий пример</span>.
         </p></span><p>2013 год начинается и заканчивается во вторник (<span class="tex-monospace">Tuesday</span>), при этом на вторник приходится <span class="tex-math-text">53</span> дня года, а на все остальные дни недели&nbsp;&ndash;— по <span class="tex-math-text">52</span> дня. Все три государственных праздника выпадают на среду (<span class="tex-monospace">Wednesday</span>). Если Илья выберет в качестве выходного дня вторник, то в году у него будет <span class="tex-math-text">53 + 3 = 56</span> выходных дней (<span class="tex-math-text">53</span> вторника и <span class="tex-math-text">3</span> государственных праздника). Если Илья выберет в качестве выходного дня среду, то у него будет только <span class="tex-math-text">52</span> выходных дня. Если же Илья выберет в качестве выходного дня любой другой день недели, то у него будет <span class="tex-math-text">52 + 3 = 55</span> выходных дней.
      </p>
      <p>Таким образом, лучший вариант для выходного дня&nbsp;&mdash; вторник, худший&nbsp;&mdash; среда, и <span style="font-weight:bold;">единственным</span> правильным ответом в данном примере является <span class="tex-monospace">Tuesday Wednesday</span>.
      </p>
      <p>Соответствие названий месяцев и дней недели в английском и русском языках:</p>
      <p><img class="user-image" src="/testsys/statement-image?imageId=1bc9b8d4e13c791b803b4a91c9b5ef2990745beefe9c2ad2253fe3fda6f0d46f"></p>
      <p>Соответствие названий месяцев и количества дней в них: </p>
      <p><img class="user-image" src="/testsys/statement-image?imageId=9f749e6620b03d62261d0032a307c1044a5e264528afa0b44ec5f02f7fc8977b"></p>
      <p>В феврале 29 дней только в високосные года. Год является високосным, если он кратен 400, либо кратен 4 и не кратен 100. Например,
         1996 и 2000 являются високосными, а 1999 и 1900 "&mdash; нет. 
      </p>
   </div>