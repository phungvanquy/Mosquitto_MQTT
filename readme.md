I. Setup for mosquitto broker:

1. Pull eclipse-mosquitto images
2. Set up volumes for important dirs in docker-compose file (inside container: /mosquitto/config, /mosquitto/log , /mosquitto/data)
3. Create /mosquitto/config/mosquitto.conf file
4. Create /mosquitto/config/pwfile (edit mosquitto/config/mosquitto.conf so that it links "password_file" to the path of pwfile)
5. Generate user:pass in pwfile with "$mosquitto_psswd -c /mosquitto/config/pwfile <username>", then enter password
6. Restart broker
7. Now we can connect to broker

II. Mqtt client
