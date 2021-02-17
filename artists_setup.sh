mkdir "./dataset" && cd ./dataset || exit
mkdir "./artists" && cd ./artists || exit
dirs='Aivazovskiy Brullov da_Vinci Mone Sezann'
for i in ${dirs}; do
  mkdir "./$i"
done