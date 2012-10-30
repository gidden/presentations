# Gnuplot script file for plotting data in file "piecewise.dat"
# This file is called plot_piecewise.p
set   autoscale                        # scale axes automatically
unset log                              # remove any log-scaling
unset label                            # remove any previous labels 
set key left                           # put the key on the left side
set xtic auto                          # set xtics automatically 
set ytic auto                          # set ytics automatically
set title "Symbolic Representation of a Piecewise Function"
set xlabel "Argument"
set ylabel "Function Value"
plot "piecewise.dat" using 1:2 title 'No Demand' with lines , \
     "piecewise.dat" using 3:4 title 'Linear Demand' with lines, \
     "piecewise.dat" using 5:6 title 'Exponential Demand' with lines
#
set terminal png
set output "piecewise.png"
replot