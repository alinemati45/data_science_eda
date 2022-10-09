library(markdown)

library(shiny)

navbarPage("QA Report!", 
           
           tabPanel("Pandas Profiling EDA Report",
                    shiny::includeHTML("./Report/ProfileReport.html")
                    
           ),
           
           tabPanel("Sweetviz Report",
                    shiny::includeHTML("./Report/SWEETVIZ_REPORT.html")
                    
           ),
           
           tabPanel("DeepCheck Report",
                    shiny::includeHTML("./Report/Deep_check.html")
           )
           
)
