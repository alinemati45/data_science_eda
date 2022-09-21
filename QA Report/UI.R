library(markdown)

library(shiny)

navbarPage("QA Report!", 
           
           tabPanel("Sweetviz Report",
                    shiny::includeHTML("./Report/SWEETVIZ_REPORT.html")
           ),
           
           tabPanel("Pandas Profiling EDA Report",
                    shiny::includeHTML("./Report/Pandas_Profiling.html")
           ),
           
           tabPanel("DeepCheck Report",
                    shiny::includeHTML("./Report/Deep_check.html")
           )
           
)
