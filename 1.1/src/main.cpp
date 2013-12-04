/*

	Copyright 2013 Zola Mahlaza (AdeebNqo) <adeebnqo@gmail.com>


*/
#include<boost/program_options.hpp>
#include<iostream>
#include<string>
int main(int argc, char* argv[]){
	using namespace boost::program_options;
	/*

	Adding the cmdline options
		
		list, l - Lists all watched directories and the processes watching them
		kill, k - kill a process watching a directories
		unwatch, u - stop watching a directory
		watch, w - watch a directory
		rwatch, r - watch a directory with its subdirectories 
	*/
	options_description opt_descr("Allowed options");
	opt_descr.add_options() ("list,l","list watched directories")
				("kill,k",value<int>(),"kill a process watching a dir")
				("unwatch,u",value<std::string>(),"Stop watching a directory")
				("watch,w",value<std::string>(),"watch a dorectory")
				("rwatch,r",value<std::string>(),"watch dir and its sub-directories");
	
	variables_map vars;
	store(parse_command_line(argc, argv, opt_descr), vars);
	notify(vars);
	
	if (vars.count("list")){
		std::cout << "listing all processes" << std::endl;
	}
	if (vars.count("kill")){
		std::cout << "killing process" << std::endl;
	}
	if (vars.count("unwatch")){
		std::cout << "unwatching dir" << std::endl;
	}
	if (vars.count("watch")){
		std::cout << "watching dir" << std::endl;
	}
	if (vars.count("rwatch")){
		std::cout << "recursively watching dir" << std::endl;
	}
	return 0;
}
