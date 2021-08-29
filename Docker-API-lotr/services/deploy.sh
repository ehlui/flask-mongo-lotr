DOCKER_COMPOSE_FILENAME="docker-compose.yml"

list_containers(){
  docker-compose ps | awk \
  'BEGIN {print "[COMMAND] :: docker-compose ps"}\
  ;{print "\033[0;32m",$0,"\033[0m"};\
  END{print "\033[0;36m...Deploy successful","\033[0m"}'
}

is_docker_compose_file(){
  FILE_NAME="${DOCKER_COMPOSE_FILENAME:-default}"
  if test -f "$FILE_NAME"; then
      return 0 # exists
  else
      return 1 # not exists
  fi
}

do_deploy(){
  docker-compose up --detach --remove-orphans
}

if is_docker_compose_file "$1";\
 then echo "Starting deployment..."; do_deploy ; list_containers; \
 else echo -e "\033[0;31m $DOCKER_COMPOSE_FILENAME \033[0m  NOT FOUND"; fi


