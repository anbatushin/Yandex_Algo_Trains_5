<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Продавец рыбы</h1>
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
         <p>Вася решил заняться торговлей рыбой. С помощью методов машинного обучения он предсказал цены на рыбу на <span class="tex-math-text">N</span> дней вперёд. Он решил, что в один день он купит рыбу, а в один из следующих дней&nbsp;&mdash; продаст (то есть совершит или ровно одну покупку и продажу или вообще не совершит покупок и продаж, если это не принесёт
            ему прибыли). К сожалению, рыба&nbsp;&mdash; товар скоропортящийся и разница между номером дня продажи и номером дня покупки не должна превышать <span class="tex-math-text">K</span>. 
         </p></span><p>Определите, какую максимальную прибыль получит Вася.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входных данных задаются числа <span class="tex-math-text">N</span> и <span class="tex-math-text">K</span> (<span class="tex-math-text">1 &le; N &le; 10000</span>, <span class="tex-math-text">1 &le; K &le; 100</span>). 
         </p></span><p>Во второй строке задаются цены на рыбу в каждый из <span class="tex-math-text">N</span> дней. Цена&nbsp;&mdash; целое число, которое может находится в пределах от 1 до <span class="tex-math-text">10<sup>9</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно число&nbsp;&mdash; максимальную прибыль, которую получит Вася.</p></span></div>
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
            <td><pre>5 2
1 2 3 4 5
</pre></td>
            <td><pre>2
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
            <td><pre>5 2
5 4 3 2 1
</pre></td>
            <td><pre>0
</pre></td>
         </tr>
      </tbody>
   </table>
</div>