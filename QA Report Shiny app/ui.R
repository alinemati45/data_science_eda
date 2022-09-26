if(!require('shinydashboard')) {
  install.packages('shinydashboard')
  library('shinydashboard')
}

function(request) {
  sidebar <- dashboardSidebar(
    hr(),
    sidebarMenu(id="tabs",
                menuItem("Pandas Profiling Report", tabName = "table", icon=icon("table"), selected=TRUE),
                menuItem("Sweetviz Report", tabName="plot", icon=icon("line-chart")),
                menuItem("About", tabName = "About", icon = icon("question"))
    ),
    hr(),
    conditionalPanel("input.tabs == 'plot'",
                     fluidRow(

            sliderInput("plot_width", "Plot width", value = 3, min = 1, max= 5, step = .5),
 
                    
                       )
                     )
    
  )
  
  body <- dashboardBody(
    tabItems(
      
      tabItem(tabName = "plot",
              shiny::includeHTML("./Report/SWEETVIZ_REPORT.html")
      ),
      tabItem(tabName = "table",
              shiny::includeHTML("./Report/SWEETVIZ_REPORT.html")
      )
        ,
      tabItem(tabName = "About",
          #shiny::includeHTML("./Report/Deep_check.html" )
      )      
      )
      
    )
  
  dashboardPage(
    dashboardHeader(title = "QA Report"),
    sidebar,
    body
  )
  
  
}
