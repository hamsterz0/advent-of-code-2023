from collections import defaultdict
import sys
import concurrent.futures
import os
import multiprocessing

filename = "input.txt"
with open(filename, 'r') as f: lines = f.read().splitlines()

def parse_input_data(lines):
    almanac = defaultdict(list)
    seeds = list()
    capture_key = None

    for line in lines:

        if not line:
            capture_key = False
            continue

        elif "seeds:" in line:
            seeds = list(map(int, line.split(": ")[1].split(" ")))

        elif "map" in line:
            capture_key = line.split(" ")[0]
        
        else:
            values = list(map(int, line.split(" ")))
            almanac[capture_key].append(values)
    
    return (seeds, almanac)

def get_dest_loc(entries, tracking):
    for entry in entries:
        dest, source, range = entry
        if source <= tracking <= source+range:
            tracking = (tracking-source)+dest
            return tracking
    return tracking


def run_through_almanac(arguments):

    init_seed, rng, almanac = arguments
    # print(f"proc id: {os.getpid()}")
    # print(init_seed, range)

    # locations = []
    location = sys.maxsize

    for seed in range(init_seed, init_seed+rng):
    
        tracking = seed

        # find the soil
        entries = almanac["seed-to-soil"]
        tracking = get_dest_loc(entries, tracking)

        # find the fert
        entries = almanac["soil-to-fertilizer"]
        tracking = get_dest_loc(entries, tracking)

        # find the water
        entries = almanac["fertilizer-to-water"]
        tracking = get_dest_loc(entries, tracking)

        # find the light
        entries = almanac["water-to-light"]
        tracking = get_dest_loc(entries, tracking)

        # find the temperature
        entries = almanac["light-to-temperature"]
        tracking = get_dest_loc(entries, tracking)

        # find the humidity
        entries = almanac["temperature-to-humidity"]
        tracking = get_dest_loc(entries, tracking)

        # find the location
        entries = almanac["humidity-to-location"]
        tracking = get_dest_loc(entries, tracking)

        # locations.append(tracking)
        location = min(location, tracking)
    
    return location

def seed_gen(init_seed, seed_range):
    for seed in range(init_seed, init_seed+seed_range):
        yield seed


# def divide_work(init_seed, rng, almanac, num_processes=61):
#     workload_per_proc = rng//num_processes + 1

#     return [(iseed, workload_per_proc, almanac) for iseed in range(init_seed, init_seed+rng, workload_per_proc)]


if __name__ == "__main__":
    seeds, almanac = parse_input_data(lines)
    location = sys.maxsize
    
    seeds = [(seed, range, almanac) for seed, range in zip(seeds[::2], seeds[1::2])]
    # print(new_seeds)
    logger = 1

    # locations = []

    # for init_seed, rng in new_seeds:
    #     print(f"[+] Started looking at the range interval {logger}")
    #     logger += 1
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # create arguments
        # arguments = divide_range_into_subsets(init_seed, rng, almanac)
        results = executor.map(run_through_almanac, seeds)

        for result in results:
            location = min(location, result)
    
    print(location)


'''

104070863 - too high. That means my division of work is now accurate. 


Tried and failed. 



    # num_processes = 61
    # # data_collected = Queue()
    # processes = []
    # for init_seed, sr in new_seeds:
    #     with multiprocessing.Pool(processes=num_processes) as pool:
    #         print(f'Input range#{logger} has started {init_seed}, {sr}')
    #         logger += 1
    #         locations = pool.starmap(run_through_almanac, [(seed, almanac) \
    #                                                        for seed in seed_gen(init_seed, sr)])
            
    #         location = min(location, min(locations))





    # trying asyncio to parralellize the problem. 
    executor = ProcessPoolExecutor(max_workers=61)

    for init_seed, sr in new_seeds:
        print(f"[+] Running range index {logger}")
        logger += 1
        data = await asyncio.gather(*(loop.run_in_executor(executor, run_through_almanac, seed, almanac) \
                                  for seed in range(init_seed, init_seed+sr)))

        location = min(location, min(data))

    print(location)
    # pool = multiprocessing.Pool(processes=60)
    # sr = seed_range
    # for init_seed, sr in new_seeds:
    #     print(f'[+]PID {os.getpid()}: Input range#{logger} has started {init_seed}, {sr}')
    #     logger += 1
    #     # locations = pool.starmap(run_through_almanac, [(seed, almanac) \
    #     #                                                for seed in seed_gen(init_seed, sr)])
    #     locations.append(pool.apply_async(run_through_almanac, (seed_gen(init_seed, sr), almanac)))
    
    # pool.close()
    # pool.join()
    # print(min(locations))

    # for seed in seeds:
    #     location = min(location, run_through_almanac(seed, almanac))

    # print(location)

'''