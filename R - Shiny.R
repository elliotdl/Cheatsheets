#SHINY
#SHINY: RENDERING
output$name <- renderPlot({
  code
  data<-reactive( code(input$ne) )
  hist( data() )
})

#SHINY: ACTION BUTTONS
#in ui fluidpage
actionButton(inputId = "clicks", label="clickme")
#in server function
observe({
  code(as.numeric(input$clicks))
})

#code outside server function once per server
#code inside server function once per end user
#code inside reactive functions (i.e. renders) once ber reaction

#HTML elements
fluidpage(
  tags$a(href= "www.google.com", "Label"),
  tags$img(height=100, width=100, src="www.imgur.com/asd.png"),
  tags$img(height=100, width=100, src="asd.png"), #image is in www folder
  HTML("htmlcode")
)

#LAYOUT
ui<-fluidPage(
  fluidrow(column(3, code), #width is always out of 12
           column(5, sliderInput(...))),
  fluidrow(column(4, offset=8, plotOutput(...))),
  tabsetPanel(
    tabPanel("label1", code),
    # tabPanel("label2", code)
  ),
  sidebarLayout(
    sidebarPanel(...),
    mainPanel(...)
  )
)

#using reactive values
server<-function(input,output){
  x<-reactiveValues()
  observe({
    x$a<- code
    x$b<- code
  })
  output$out <- renderPlot({
    barplot(x$a)})
}

x<-reactive({ input$foo1+input$foo2 })
output$foo3 <- renderPlot( x() ) #NEED x() not x!

#SHINY TEMPLATE
library(shiny)

ui<-fluidPage(
  numericInput(inputId="a", label=NULL, value=0),
  textOutput(outputId="out")
)

server <- function(input, output) {
  y<-(input$a)
  output$out <- renderText({y})
}

shinyApp(ui = ui, server = server)