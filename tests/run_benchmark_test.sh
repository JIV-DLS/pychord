
#declare -a arr=("sudo yum search zsh" "sudo yum list zsh")
eval "docker build . -t test_python"

for (( i = 0; i < 5 ; i++ )); do
    printf "\n**** Running: docker run -it -e NODES_SIZE=5 test_python *****\n\n"

    eval "docker run -it -e NODES_SIZE=5 test_python"

done
for (( i = 0; i < 5 ; i++ )); do
    printf "\n**** Running: docker run -it -e NODES_SIZE=10 test_python *****\n\n"

    eval "docker run -it -e NODES_SIZE=10 test_python"

done
for (( i = 0; i < 5 ; i++ )); do
    printf "\n**** Running: docker run -it -e NODES_SIZE=25 test_python *****\n\n"

    eval "docker run -it -e NODES_SIZE=25 test_python"
done