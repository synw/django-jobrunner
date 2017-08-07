package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"github.com/synw/centcom"
	"os/exec"
)

var path = flag.String("path", "", "Base dir")
var addr = flag.String("addr", "localhost:8001", "Centrifugo address")
var key = flag.String("key", "secret_key", "Centrifugo secret key")
var channelIn = flag.String("cmd_in", "$commands_in", "Channel in")
var channelOut = flag.String("cmd_out", "$commands_out", "Channel out")
var verbosity = flag.Int("v", 1, "Verbosity")

var cli *centcom.Cli
var chanOut string

func runCmd(jobName string, jobId string) {
	msg := "Starting job " + jobName + " (" + jobId + ")"
	class := "__job_start__"
	rprint(msg, class)
	out, err := exec.Command("./run.sh", jobName).Output()
	if err != nil {
		panic(err)
	}
	fmt.Println(string(out))
	msg = "Job " + jobName + " (" + jobId + ")" + " is finished"
	class = "__job_end__"
	rprint(msg, class)
}

func rprint(msg string, class string) {
	d := make(map[string]string)
	d["message"] = msg
	d["event_class"] = class
	dataBytes, err := json.Marshal(d)
	if err != nil {
		fmt.Println(err)
	}
	ok, err := cli.Http.Publish(chanOut, dataBytes)
	if err != nil {
		fmt.Println(err, ok)
	}
	fmt.Println(msg)
}

func listen() {
	flag.Parse()
	chanOut = *channelOut
	// connect
	cli = centcom.New(*addr, *key)
	err := centcom.Connect(cli)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer centcom.Disconnect(cli)
	err = cli.Subscribe(*channelIn)
	if err != nil {
		fmt.Println(err)
	}
	// listen
	fmt.Println("Ready, waiting for jobs ...")
	for msg := range cli.Channels {
		if msg.Channel == *channelIn {
			p := msg.Payload.(map[string]interface{})
			data := p["data"].(map[string]interface{})
			jobName := data["cmd"].(string)
			jobId := data["uid"].(string)
			//args := data["args"].(string)
			msg := "=> Incoming command " + jobName
			fmt.Println(msg)
			go runCmd(jobName, jobId)
		}
	}
}

func main() {
	go listen()
	select {}
}
