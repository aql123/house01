/*------------------------------------------------------
    Author : www.webthemez.com
    License: Commons Attribution 3.0
    http://creativecommons.org/licenses/by/3.0/
---------------------------------------------------------  */

(function ($) {
    "use strict";
    var mainApp = {

        initFunction: function () {
            /*MENU 
            ------------------------------------*/
            $('#main-menu').metisMenu();
			
            $(window).bind("load resize", function () {
                if ($(this).width() < 768) {
                    $('div.sidebar-collapse').addClass('collapse')
                } else {
                    $('div.sidebar-collapse').removeClass('collapse')
                }
            });

            /* MORRIS BAR CHART
			-----------------------------------------*/
            Morris.Bar({
                element: 'morris-bar-chart',
                data: [{
                    y: '北京',
                    a: 456,
                    b: 2501
                }, {
                    y: '上海',
                    a: 507,
                    b: 1325
                }, {
                    y: '广州',
                    a: 514,
                    b: 1987
                }, {
                    y: '深圳',
                    a: 256,
                    b: 2743
                },],
                xkey: 'y',
                ykeys: ['a', 'b'],
                labels: ['无燃气', '有燃气'],
				 barColors: [
    '#A6A6A6','#F09B22',
    '#A8E9DC' 
  ],
                hideHover: 'auto',
                resize: true
            });
	 


            /* MORRIS DONUT CHART
			----------------------------------------*/
            Morris.Donut({
                element: 'morris-donut-chart',
                data: [{
                    label: "有电梯",
                    value: 7114
                }, {
                    label: "无电梯",
                    value: 3632
                }, {
                    label: "暂无数据",
                    value: 1
                }],
				   colors: [
    '#A6A6A6','#F09B22',
    '#A8E9DC' 
  ],
                resize: true
            });

            /* MORRIS AREA CHART
			----------------------------------------*/

            Morris.Area({
                element: 'morris-area-chart',
                data: [{
                    period: '1.十室2厅5卫 ',
                    sz: 1,
                    bj: null,
                    sh: null,
                    gz: null
                }, {
                    period: '2.一室0厅0卫',
                    sz: 41,
                    bj: 60,
                    sh: null,
                    gz: 46
                }, {
                    period: '3.一室0厅1卫',
                    sz: 341,
                    bj: 51,
                    sh: 141,
                    gz: 146
                }, {
                    period: '4.一室1厅1卫',
                    sz: 453,
                    bj: 170,
                    sh: 418,
                    gz: 369
                }, {
                    period: '5.一室1厅2卫',
                    sz: 1,
                    bj:13,
                    sh: null,
                    gz: null
                }, {
                    period: '6.一室2厅1卫',
                    sz: 62,
                    bj: null,
                    sh: null,
                    gz: 31
                }, {
                    period: '7.二室0厅0卫',
                    sz: 8,
                    bj: null,
                    sh: 45,
                    gz: null
                }, {
                    period: '8.二室1厅1卫',
                    sz: 381,
                    bj: 975,
                    sh: 424,
                    gz: 432
                }, {
                    period: '9.二室1厅2卫',
                    sz: 18,
                    bj: 51,
                    sh: null,
                    gz: 16
                }, {
                    period: '10.二室2厅1卫 ',
                    sz: 217,
                    bj: 97,
                    sh: 192,
                    gz: 94
                },{
                    period: '11.二室2厅2卫',
                    sz: 169,
                    bj: 63,
                    sh: 43,
                    gz: 8
                },{
                    period: '12.三室1厅1卫',
                    sz: 149,
                    bj: 287,
                    sh: 154,
                    gz: 178
                },{
                    period: '13.三室1厅2卫',
                    sz: 116,
                    bj: 97,
                    sh: 39,
                    gz: 35
                },{
                    period: '14.三室2厅1卫',
                    sz: 221,
                    bj: 61,
                    sh: 93,
                    gz: 140
                },{
                    period: '15.三室2厅2卫',
                    sz: 298,
                    bj: 144,
                    sh: 203,
                    gz: 240
                }, {
                    period: '16.三室2厅3卫',
                    sz: 20,
                    bj: 26,
                    sh: 18,
                    gz: null
                }, {
                    period: '17.四室1厅1卫',
                    sz: 30,
                    bj: 1,
                    sh: null,
                    gz: 241
                }, {
                    period: '18.四室1厅2卫',
                    sz: 81,
                    bj: 46,
                    sh: 1,
                    gz: 317
                }, {
                    period: '19.四室1厅3卫',
                    sz: 1,
                    bj: 94,
                    sh: null,
                    gz: null
                }, {
                    period: '20.四室2厅1卫',
                    sz: 3,
                    bj: 1,
                    sh: null,
                    gz: 75
                }, {
                    period: '21.四室2厅2卫',
                    sz: 269,
                    bj: 125,
                    sh: 64,
                    gz: 75
                }, {
                    period: '22.四室2厅3卫',
                    sz: 12,
                    bj: 94,
                    sh: 30,
                    gz: 71
                }, {
                    period: '23.四室2厅4卫',
                    sz: 13,
                    bj: 42,
                    sh: 14,
                    gz: 1
                }, {
                    period: '24.五室1厅5卫',
                    sz: 23,
                    bj: null,
                    sh: null,
                    gz: null
                }, {
                    period: '25.五室2厅1卫',
                    sz: 14,
                    bj: null,
                    sh: null,
                    gz: null
                }, {
                    period: '26.五室2厅2卫',
                    sz: 10,
                    bj: 37,
                    sh: null,
                    gz: 124
                }, {
                    period: '27.五室2厅3卫',
                    sz: 298,
                    bj: 26,
                    sh: 23,
                    gz: 29
                }, {
                    period: '28.六室3厅2卫',
                    sz: 19,
                    bj: 24,
                    sh: 1,
                    gz: 14
                }, {
                    period: '29.八室2厅2卫',
                    sz: 1,
                    bj: null,
                    sh: 16,
                    gz: null
                }, {
                    period: '30.八室3厅7卫',
                    sz: 19,
                    bj: null,
                    sh: 19,
                    gz: null
                }, ],
                xkey: 'period',
                ykeys: ['sz', 'bj', 'sh','gz'],
                labels: ['深圳', '北京', '上海','广州'],
                pointSize: 2,
                hideHover: 'auto',
				  pointFillColors:['#ffffff'],
				  pointStrokeColors: ['black'],
				  lineColors:['#A6A6A6','#F09B22'],
                resize: true
            });

            /* MORRIS LINE CHART
			----------------------------------------*/
            Morris.Line({
                element: 'morris-line-chart',
                data: [
					  { y: '1北京', a: 11723},
					  { y: '2上海', a: 10381},
					  { y: '3广州', a: 4492},
					  { y: '4深圳', a: 5635},
				],
            
				 
      xkey: 'y',
      ykeys: ['a'],
      labels: ['平均月租金'],
      fillOpacity: 0.6,
      hideHover: 'auto',
      behaveLikeLine: true,
      resize: true,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','#F09B22']
	  
            });
           
        
            $('.bar-chart').cssCharts({type:"bar"});
            $('.donut-chart').cssCharts({type:"donut"}).trigger('show-donut-chart');
            $('.line-chart').cssCharts({type:"line"});

            $('.pie-thychart').cssCharts({type:"pie"});
       
	 
        },

        initialization: function () {
            mainApp.initFunction();

        }

    }
    // Initializing ///

    $(document).ready(function () {
        mainApp.initFunction(); 
		$("#sideNav").click(function(){
			if($(this).hasClass('closed')){
				$('.navbar-side').animate({left: '0px'});
				$(this).removeClass('closed');
				$('#page-wrapper').animate({'margin-left' : '260px'});
				
			}
			else{
			    $(this).addClass('closed');
				$('.navbar-side').animate({left: '-260px'});
				$('#page-wrapper').animate({'margin-left' : '0px'}); 
			}
		});
    });

}(jQuery));
