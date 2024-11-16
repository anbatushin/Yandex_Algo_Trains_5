<div class="problem-statement">
   <div class="header">
      <h1 class="title">H. Спички детям не игрушка!</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
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
         <p>Вася любит решать головоломки со спичками. Чаще всего они формулируется следующим образом: дано изображение <span class="tex-math-text">A</span>, составленное из спичек; переложите в нем минимальное количество спичек так, чтобы получилось изображение <span class="tex-math-text">B</span>. 
         </p></span><p>Например, из номера текущего командного чемпионата школьников Санкт-Петербурга по программированию, можно получить ромб с
         диагональю, переложив всего три спички.
      </p>
      <p>
         <div style="text-align:center;"><img class="user-image" src="/testsys/statement-image?imageId=19e8753f7af3e8177364a572d3f003010c7aebc5ad2417c8bf27b39b5ddc2437"> 
         </div>
      </p>
      <p>Головоломки, которые решает Вася, всегда имеют решение. Это значит, что набор спичек, используемый в изображении <span class="tex-math-text">A</span>, совпадает с набором спичек, используемым в изображении <span class="tex-math-text">B</span>. Кроме того, в одном изображении никогда не встречаются две спички, у которых есть общий участок ненулевой длины (то есть
         спички могут пересекаться, но не могут накладываться друг на друга).
      </p>
      <p>Вася устал решать головоломки вручную, и теперь он просит вас написать, программу, которая будет решать головоломки за него.
         Программа будет получать описания изображений <span class="tex-math-text">A</span> и <span class="tex-math-text">B</span> и должна найти минимальное количество спичек, которые надо переложить в изображении <span class="tex-math-text">A</span>, чтобы полученная картинка получалась из <span class="tex-math-text">B</span> параллельным переносом. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла содержится целое число <span class="tex-math-text">n</span> &mdash; количество спичек в каждом из изображений (<span class="tex-math-text">1 &le; n &le; 1000</span>).
         </p></span><p>В следующих <span class="tex-math-text">n</span> строках записаны координаты концов спичек на изображении <span class="tex-math-text">A</span>. Спичка номер&nbsp;<span class="tex-math-text">i</span> описывается целыми числами <span class="tex-math-text">x<sub>1i</sub></span>, <span class="tex-math-text">y<sub>1i</sub></span>, <span class="tex-math-text">x<sub>2i</sub></span>, <span class="tex-math-text">y<sub>2i</sub></span>&nbsp;&mdash; координатами ее концов. Следующие <span class="tex-math-text">n</span> строк содержат описание изображения <span class="tex-math-text">B</span> в таком же формате. Набор длин этих спичек совпадает с набором длин спичек с изображения&nbsp;<span class="tex-math-text">A</span>.
      </p>
      <p>Все координаты по абсолютной величине не превосходят <span class="tex-math-text">10<sup>4</sup></span>. Все спички имеют ненулевую длину, то есть <span class="tex-math-text">x<sub>1i</sub> &ne; x<sub>2i</sub></span> или <span class="tex-math-text">y<sub>1i</sub> &ne; y<sub>2i</sub></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите в выходной файл минимальное количество спичек, которые следует переложить, чтобы изображение <span class="tex-math-text">A</span> совпало с изображением <span class="tex-math-text">B</span>, с точностью до параллельного переноса.
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
            <td><pre>5
0 0 1 2
1 0 0 2
2 0 2 2
4 0 3 2
4 0 5 2
9 -1 10 1
10 1 9 3
8 1 10 1
8 1 9 -1
8 1 9 3
</pre></td>
            <td><pre>3
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
            <td><pre>1
3 4 7 9
-1 3 3 8
</pre></td>
            <td><pre>0
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
            <td><pre>1
-4 5 2 -3
-12 4 -2 4
</pre></td>
            <td><pre>1
</pre></td>
         </tr>
      </tbody>
   </table>