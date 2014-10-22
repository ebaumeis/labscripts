# uses gnuplot to plot entries from a .log NAMD output file
# first argument is the .log file to be analyzed, second argument is the quantity to be plotted
# third argument is the filename

grep "^ENERGY: " $1 | awk '{$1 = ""; print $0}' > data



if [[ "$2" == "energy" ]]; then
	gnuplot /home/ebaumeis/Documents/gplotScripts/plotEnergy
elif [[ "$2" == "pressure" ]]; then
	gnuplot /home/ebaumeis/Documents/gplotScripts/plotPressure
elif [[ "$2" == "temp" ]]; then
	gnuplot /home/ebaumeis/Documents/gplotScripts/plotTemp
else
	echo "invalid second argument"
fi

mv output.png $3
