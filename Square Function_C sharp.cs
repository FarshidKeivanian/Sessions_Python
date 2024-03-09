using System;
using OxyPlot;
using OxyPlot.Series;
using OxyPlot.Axes;

namespace SquareFunctionPlot
{
    class Program
    {
        static void Main(string[] args)
        {
            var model = new PlotModel { Title = "Plot of the function f(x) = x^2" };

            // Adding the axes
            model.Axes.Add(new LinearAxis { Position = AxisPosition.Bottom, Title = "x" });
            model.Axes.Add(new LinearAxis { Position = AxisPosition.Left, Title = "f(x)" });

            var series = new FunctionSeries(x => x * x, -10, 10, 0.05, "f(x) = x^2");
            model.Series.Add(series);

            // Generate plot model with OxyPlot
            var plotView = new OxyPlot.WindowsForms.PlotView
            {
                Model = model,
                Dock = System.Windows.Forms.DockStyle.Fill
            };

            // Creating a simple Windows Forms window to display the plot
            var form = new System.Windows.Forms.Form();
            form.Controls.Add(plotView);
            form.ShowDialog();
        }
    }
}
