#!/bin/bash
cd "./dataset/artists/" || exit
dirs=($(ls -d */))
declare -A files_to
files_to["Aivazovskiy/"]='https://upload.wikimedia.org/wikipedia/commons/2/26/Ivan_Constantinovich_Aivazovsky_-_The_Russian_Squadron_on_the_Sebastopol_Roads.jpg https://upload.wikimedia.org/wikipedia/commons/c/cb/%D0%98%D0%B2%D0%B0%D0%BD_%D0%9A._%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_-_%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B0%D1%8F_%D0%9F%D0%B8%D1%80%D0%B0%D0%BC%D0%B8%D0%B4%D0%B0_%D0%B2_%D0%93%D0%B8%D0%B7%D0%B5_%281871%29.jpg https://upload.wikimedia.org/wikipedia/commons/e/e1/Bayron%27s_visit_to_San_Lazzaro_by_Aivazovsky_%281899%29.jpg https://upload.wikimedia.org/wikipedia/commons/7/76/Stormy_sea_at_night.jpg'
files_to["Brullov/"]='https://upload.wikimedia.org/wikipedia/commons/9/9d/Brjullov_Italianskoe_Utro.jpg https://upload.wikimedia.org/wikipedia/commons/a/a6/1832._BRULLOV_VSADNICA1.jpg https://upload.wikimedia.org/wikipedia/commons/f/f7/Bryullov_Portrait_of_General_Petrovsky_V.A..jpg https://upload.wikimedia.org/wikipedia/commons/b/b6/Karl_Brullov_05.jpeg'
files_to["da_Vinci/"]='https://upload.wikimedia.org/wikipedia/commons/6/6f/Leonardo_da_Vinci_attributed_-_Madonna_Litta.jpg https://upload.wikimedia.org/wikipedia/commons/7/70/Leonardo_da_Vinci_Madonna_of_the_Carnation.jpg https://upload.wikimedia.org/wikipedia/commons/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg https://upload.wikimedia.org/wikipedia/commons/b/bc/Andrea_del_Verrocchio%2C_Leonardo_da_Vinci_-_Baptism_of_Christ_-_Uffizi.jpg'
files_to["Mone/"]='https://upload.wikimedia.org/wikipedia/commons/3/31/Claude_Monet_023.jpg https://upload.wikimedia.org/wikipedia/commons/a/a3/Monet_Japonaise.jpg https://upload.wikimedia.org/wikipedia/commons/9/96/La_Gare_Saint-Lazare_-_Claude_Monet.jpg https://upload.wikimedia.org/wikipedia/commons/6/6b/Nympheas_71293_3.jpg'
files_to["Sezann/"]='https://upload.wikimedia.org/wikipedia/commons/d/db/Jeune_Fille_au_piano%2C_par_Paul_C%C3%A9zanne.jpg https://upload.wikimedia.org/wikipedia/commons/a/ac/Bord_de_la_Marne%2C_par_Paul_C%C3%A9zanne%2C_Hermitage_Museum.jpg https://upload.wikimedia.org/wikipedia/commons/c/ca/Homme_%C3%A0_la_pipe%2C_par_Paul_C%C3%A9zanne%2C_Mus%C3%A9e_de_l%27Ermitage.jpg'
for i in "${dirs[@]}"; do
  cd "./$i" || return
  pwd
  for j in ${files_to["$i"]}; do
    echo "$j"
    wget "$j"
    done
  cd ".."
done
