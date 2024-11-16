<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Саруман</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>4&nbsp;секунды</td>
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
         <p>Как известно, Саруман Радужный очень любит порядок. Поэтому все полки его войска стоят друг за другом, причем каждый следующий
            полк содержит количество орков не меньше, чем предыдущий.
         </p></span><p>Перед тем как напасть на Хельмову Падь, Саруман решил провести несколько вылазок для разведки. Чтобы его отряды никто не заметил,
         он решил каждый раз отправлять несколько подряд идущих полков так, чтобы суммарное количество орков в них было равно определенному
         числу. Так как это всего лишь разведка, каждый полк после вылазки возвращается на свое место. Задачу выбрать нужные полки
         он поручил Гриме Змеиному Языку. А Грима не поскупится на вознаграждение, если вы ему поможете. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла находится два целых числа: <span class="tex-math-text">n</span> (<span class="tex-math-text">1 &le; n &le; 2&#x22C5;10<sup>5</sup></span>)&nbsp;&mdash; количество полков и <span class="tex-math-text">m</span> (<span class="tex-math-text">1 &le; m &le; 2&#x22C5;10<sup>5</sup></span>)&nbsp;&ndash; количество предстоящих вылазок.
         </p></span><p>В следующей строке записано <span class="tex-math-text">n</span> чисел <span class="tex-math-text">a<sub>i</sub></span>, где <span class="tex-math-text">a<sub>i</sub></span>&nbsp;&mdash; число орков в <span class="tex-math-text">i</span>-ом полке (<span class="tex-math-text">1 &le; a<sub>i</sub> &le; 10<sup>9</sup>, a<sub>i</sub> &le; a<sub>i+1</sub></span>).
      </p>
      <p>Далее в <span class="tex-math-text">m</span> строках записаны запросы вида: количество полков <span class="tex-math-text">l</span> (<span class="tex-math-text">1 &le; l &le; n</span>), которые должны будут отправиться в эту вылазку, и суммарное количество орков в этих полках <span class="tex-math-text">s</span> (<span class="tex-math-text">1 &le; s &le; 2&#x22C5;10<sup>16</sup></span>) 
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса выведите номер полка, с которого начнутся те <span class="tex-math-text">l</span>, которые необходимо отправить на вылазку. Если таких полков несколько, выведите любой. Если же так выбрать полки нельзя,
            выведите <span class="tex-math-text">-1</span>.
         </p></span></div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5 2
1 3 5 7 9
2 4
1 3
</pre></td>
            <td><pre>1
2
</pre></td>
         </tr>
      </tbody>
   </table>